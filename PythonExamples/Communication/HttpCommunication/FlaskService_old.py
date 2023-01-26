import datetime
import multiprocessing
import threading
import time
from multiprocessing import Event, Process
from typing import Dict, Any

from flask import Flask, request, app
from flask_cors import CORS
import atexit

from Logging.ConsoleLogger import ConsoleLogger
from Logging.LoggerBase import LoggerBase


class FlaskService:
    # class members
    flaskApp = Flask(__name__, template_folder='templates')

    def __init__(self, logger):
        self.logger: LoggerBase = logger
        atexit.register(self.flaskServiceExited)
        self.flaskProcess: Process = None
        self._parentQueue = multiprocessing.Queue
        self._child_queue = multiprocessing.Queue
        self._eventsDict: Dict[str, Event] = {}
        self._responseDict: Dict[str, str] = {}
        self._uniqueueKey = 1000
        self._uniqueKeyLock = threading.RLock()

    def flaskServiceExited(self):
        self.logger.logInfo('FlaskService process is closing')

    def startServiceProcess(self):
        self.flaskProcess = Process(target=self._process_func, args=(self.logger,))
        self.flaskProcess.start()

    def stopServiceProcess(self):
        self.flaskProcess.terminate()

    @staticmethod
    def _process_func(logger: LoggerBase):
        logger.logInfo('Flask service is starting')
        FlaskService.flaskApp.config['SECRET_KEY'] = 'secret!'
        FlaskService.flaskApp.config['CORS_HEADERS'] = 'Content-Type'
        cors = CORS(FlaskService.flaskApp)  # TODO: taken from DIX application, no idea what this declaration does

        FlaskService.flaskApp.add_url_rule()
        FlaskService.flaskApp.run(debug=True, host='10.108.102.29', port=8080, threaded=True)

    @staticmethod
    @flaskApp.route('/', defaults={'path': ''})
    @flaskApp.route('/<path:path>', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def home(path):
        return f'hello {path}'


if __name__ == '__main__':
    print('main')
    service = FlaskService(ConsoleLogger())
    service.startServiceProcess()
    # service.stopServiceProcess()
