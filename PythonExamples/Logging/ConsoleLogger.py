import datetime

from Logging.LoggerBase import LoggerBase


class ConsoleLogger(LoggerBase):
    @staticmethod
    def _printText(prefix, text):
        print(f'{prefix} [{datetime.datetime.now().time()}] {text}')

    def logDebug(self, text):
        self._printText('D', text)

    def logError(self, text):
        self._printText('E', text)

    def logWarn(self, text):
        self._printText('W', text)

    def logInfo(self, text):
        self._printText('I', text)
