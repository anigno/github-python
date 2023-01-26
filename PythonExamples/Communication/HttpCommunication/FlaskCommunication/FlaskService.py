from threading import Thread, RLock, Event
from multiprocessing import Queue, Process
from flask import Flask, Response, request
from flask_cors import CORS

from Logging.ConsoleLogger import ConsoleLogger
from Logging.LoggerBase import LoggerBase

from Communication.HttpCommunication.FlaskCommunication.RequestData import RequestData
from Communication.HttpCommunication.FlaskCommunication.ResponseData import ResponseData


class FlaskService:
    """Application service to handle HTTP requests delivered by IPC (queues) and maintain order by using generated keys"""

    def __init__(self, name: str, host: str, port: int, requestQueue: Queue, responseQueue: Queue, logger: LoggerBase = ConsoleLogger(),responseTimeoutSec=60):
        self._responseQueue = responseQueue
        self._requestQueue = requestQueue
        self._port = port
        self._host = host
        self._logger = logger
        self.responseTimeoutSec = responseTimeoutSec
        self._uniqueueKey = 1000
        self._uniqueKeyLock = RLock()
        self._responseThread: Thread = None
        self._eventDictionary = {}
        self._responseDataDictionary = {}
        # init functions
        self._initFlaskApp(name)
        self._mapUrls()

    def _initFlaskApp(self, name):
        """Initialize the flask application"""
        self._logger.logDebug('Flask service initializing')
        self.flaskApp = Flask(name)
        self.flaskApp.config['SECRET_KEY'] = 'secret'
        self.flaskApp.config['CORS_HEADERS'] = 'Content-Type'
        CORS(self.flaskApp)
        self._responseThread = Thread(target=self.responseThreadFunction, name='responseThread')
        self._logger.logDebug('Flask service initialized')

    def _mapUrls(self):
        """Map URL path for the flask application"""
        self.flaskApp.add_url_rule(rule='/', endpoint='nothing', view_func=self._action, methods=['POST', 'PUT', 'DELETE', 'GET'])
        self.flaskApp.add_url_rule(rule='/<path:path>', endpoint='allPath', view_func=self._action, methods=['POST', 'PUT', 'DELETE', 'GET'])

    def responseThreadFunction(self):
        """Thread function for receiving responses from the application"""
        while True:
            responseData: ResponseData = self._responseQueue.get()
            self._logger.logDebug(f'Service response {responseData}')
            self._responseDataDictionary[responseData.Key] = responseData
            keyEvent: Event = self._eventDictionary[responseData.Key]
            keyEvent.set()

    def _getUniqueueKey(self) -> str:
        """Generate a unique key, thread safe"""
        with self._uniqueKeyLock:
            self._uniqueueKey += 1
            return str(self._uniqueueKey)

    def _action(self, path: str = 'None'):
        """Delegate function mapped for all incoming HTTP requests"""
        jsonData = request.get_json()
        method = request.method
        key = self._getUniqueueKey()
        keyEvent = Event()
        self._eventDictionary[key] = keyEvent
        requestData = RequestData(key, method, path, jsonData)
        self._logger.logDebug(f"Service requested {requestData}")
        self._requestQueue.put(requestData)
        isSignaled = keyEvent.wait(self.responseTimeoutSec)
        self._eventDictionary.pop(requestData.Key, None)
        if not isSignaled:
            self._logger.logWarn(f"Response wasn't received for [{requestData}")
            return Response(response=f"Response wasn't received for{requestData}", status='404')
        responseData: ResponseData = self._responseDataDictionary.pop(key)
        response = Response(response=responseData.Json, status=responseData.Code)
        self._logger.logDebug(f'Service Ended handling {responseData.Key} {responseData.Code}')
        return response

    def start(self):
        self._responseThread.start()
        self.flaskApp.run(host=self._host, port=self._port, threaded=True)

    @staticmethod
    def startFlaskProcess(requestQueue, responseQueue):
        """Flask process start function"""
        flaskService = FlaskService(name='wrap', host='10.108.102.29', port=8080, requestQueue=requestQueue, responseQueue=responseQueue,logger=ConsoleLogger())
        flaskService.start()
