from abc import ABC, abstractmethod


class LoggerBase(ABC):
    @abstractmethod
    def logDebug(self, text):
        pass

    @abstractmethod
    def logError(self, text):
        pass

    @abstractmethod
    def logWarn(self, text):
        pass

    @abstractmethod
    def logInfo(self, text):
        pass


