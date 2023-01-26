import datetime
import time
from threading import Thread
from LoggerBase import LoggerBase
import asyncio

class TaskScheduler:
    def __init__(self, logger: LoggerBase, sampleInterval: float):
        self.sampleInterval = sampleInterval
        self._schedulerThread = Thread(target=self.schedulerThreadStart)
        self.logger = logger
        self._tasksDictionary={}
        self._mainLoop=asyncio.

    def AddTask(self, task, periodic: float, interval: float, *args, **kwargs):
        """
        Add new task function
        :param task: function to run
        :param periodic: time in seconds to schedule running
        :param interval: time in seconds to let task run in each schedule
        :param args: any specific arguments
        :param kwargs: any named arguments
        """
        self._tasksDictionary

    def Start(self):
        """
        Start scheduler
        """
        self._schedulerThread.start()

    def schedulerThreadStart(self, *args):
        pass
