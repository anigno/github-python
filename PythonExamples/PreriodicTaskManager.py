import time
from threading import Thread
from Logging.ConsoleLogger import ConsoleLogger
from Logging.LoggerBase import LoggerBase
import math


class PreriodicTaskManager:
    def __init__(self, logger: LoggerBase):
        self.logger = logger
        self._tasksThreads = []

    def AddTask(self, name: str, periodic: float, count: int, taskFunction, functionArgs: tuple):
        taskThread = Thread(target=self.taskFunction, args=(name, periodic, count, taskFunction, functionArgs))
        self._tasksThreads.append(taskThread)

    def Start(self):
        for taskThread in self._tasksThreads:
            taskThread.start_receiving()

    def taskFunction(self, name, periodic, count, taskFunction, functionArgs):
        cnt = 0
        while True:
            taskFunction(*functionArgs)
            cnt += 1
            if cnt >= count:
                self.logger.logDebug(f'-end-{name}')
                t0 = time.clock()
                time.sleep(periodic)
                dt = time.clock() - t0
                if dt > periodic * 1.2:  # 20% timeout margin
                    self.logger.logWarn(f'{name} periodic timeout {dt} / {periodic}')
                cnt = 0


if __name__ == '__main__':
    consoleLogger = ConsoleLogger()


    def doSomething(name: str, workCnt):
        consoleLogger.logDebug(name)
        for a in range(workCnt):
            math.sqrt(a)


    scheduler = PreriodicTaskManager(consoleLogger)
    scheduler.AddTask('TaskA', 0.2, 5, doSomething, ('Task A', 300000))
    scheduler.AddTask('TaskB', 0.2, 5, doSomething, ('Task B', 300000))
    scheduler.AddTask('TaskC', 0.5, 10, doSomething, ('Task C', 400000))
    scheduler.Start()
