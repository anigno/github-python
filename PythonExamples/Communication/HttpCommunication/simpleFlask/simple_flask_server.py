from flask import Flask, request
from flask_cors import CORS

flaskApp = Flask(__name__)
flaskApp.config['SECRET_KEY'] = 'secret!'
flaskApp.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(flaskApp)


def action(path=''):
    data=request.data
    print(path,data)
    return path

def mapUrls():
    """Map URL path for the flask application"""
    flaskApp.add_url_rule(rule='/', endpoint='nothing', view_func=action, methods=['POST', 'PUT', 'DELETE', 'GET'])
    flaskApp.add_url_rule(rule='/<path:path>', endpoint='allPath', view_func=action, methods=['POST', 'PUT', 'DELETE', 'GET'])

def process_func():
    flaskApp.run(host='127.0.0.1', port=5555, debug=False, threaded=True)

mapUrls()
process_func()