import datetime
import multiprocessing
import threading
import time
from multiprocessing import Event
from typing import Dict, Any

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

_parentQueue: multiprocessing.Queue = None
_child_queue: multiprocessing.Queue = None
_eventsDict: Dict[str, Event] = {}
_responseDict: Dict[str, str]={}
_uniqueueKey=1000
_uniqueKeyLock=threading.RLock()

def getUniqueueKey():
    global _uniqueueKey,_uniqueKeyLock
    with _uniqueKeyLock:
        _uniqueueKey+=1
        return str(_uniqueueKey)

def addKey(message: str) -> ('str', 'str'):
    # key = str(datetime.datetime.now().time())
    key=getUniqueueKey()
    messageWithKey = f'#{key}#{message}'
    return key, messageWithKey


def extractMessageKey(messageWithKey: str) -> ('str', 'str'):
    a = messageWithKey.find('#', 0)
    b = messageWithKey.find('#', a + 1)
    key = messageWithKey[a + 1:b]
    message = messageWithKey[b + 1:]
    return key, message


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home(path):
    key, keyAndRequest = addKey(request.data)
    event = Event()
    _eventsDict[key] = event
    _parentQueue.put_nowait(keyAndRequest)
    print(datetime.datetime.now().time(), 'server', 'waiting', keyAndRequest, path)
    event.wait()
    print(datetime.datetime.now().time(), 'server', 'event set', keyAndRequest)
    response=_responseDict.pop(key)
    return response


def appListenerStartMethod():
    global _responseDict
    while(True):
        if _child_queue.empty():
            time.sleep(0.001)
        else:
            keyAndResponse = _child_queue.get_nowait()
            print(datetime.datetime.now().time(), 'server', 'will set', keyAndResponse)
            key, message = extractMessageKey(keyAndResponse)
            try:
                event=_eventsDict.pop(key)
                _responseDict[key]=message
                event.set()
            except Exception as ex:
                print(key,ex,ex.args)


def process_func(parentQueue, child_queue):
    global _parentQueue, _child_queue
    _parentQueue = parentQueue
    _child_queue = child_queue
    threading.Thread(target=appListenerStartMethod).start()
    app.run(debug=True, host='10.108.102.29', port=8080, threaded=True)
