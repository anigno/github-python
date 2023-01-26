from multiprocessing import Queue, Process
from threading import Thread

from Communication.HttpCommunication.FlaskCommunication import FlaskService
from Communication.HttpCommunication.FlaskCommunication.RequestData import RequestData
from Communication.HttpCommunication.FlaskCommunication.ResponseData import ResponseData
from Logging.ConsoleLogger import ConsoleLogger
from Logging.LoggerBase import LoggerBase


class FlaskCommunicator:
    def __init__(self, responseDataProducerFunction, logger: LoggerBase = ConsoleLogger()):
        """
        Provide an application interface for using HTTP communication
        :type responseDataProducerFunction: function that receive RequestData and return ResponseData
        """
        self.logger = logger
        self.requestQueue = Queue(-1)
        self.responseQueue = Queue(-1)
        self.responseDataProducerFunction = responseDataProducerFunction

    def start(self):
        p = Process(target=FlaskService.FlaskService.startFlaskProcess, args=(self.requestQueue, self.responseQueue))
        p.start()
        communicatorThread = Thread(target=self.communicatorThreadFunction)
        communicatorThread.start()

    def communicatorThreadFunction(self):
        while True:
            requestData: RequestData = self.requestQueue.get()
            self.logger.logDebug(f'application requested {requestData}')
            response = self.responseDataProducerFunction(requestData)
            self.responseQueue.put(response)


if __name__ == '__main__':
    logger = ConsoleLogger()


    def responseDataProducerFunction(requestData):
        logger.logDebug(requestData)
        return ResponseData(requestData.Key, '200', '{"application":"answer"}')


    communicator = FlaskCommunicator(logger=logger, responseDataProducerFunction=responseDataProducerFunction)
    communicator.start()
