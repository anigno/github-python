import socket
import time
import heapq
from threading import Thread

from Communication.Udp import LoggerBase
from Communication.Udp.ConsoleLogger import ConsoleLogger
from Communication.Udp.PriorityQueue import PriorytyQueue, PriorityQueueItem


class UdpSender:
    """
    message structure:
        [crc(B)][counter(B)][part(B)][parts(B)][data(0-16M)]
    """

    def __init__(self, logger: LoggerBase, sendIp: str, sendPort: int, localPort: int, maxPriorityLevels: int):
        self._logger = logger
        self._sendPort = sendPort
        self._localPort = localPort
        self._sendIp = sendIp
        self._receiveBufferSize = 1024
        self._sendSocket = None
        self._sendThread = None
        self._sendQueue = PriorytyQueue(maxPriorityLevels=maxPriorityLevels)

    def Init(self):
        self._sendSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._sendSocket.bind((self._sendIp, self._localPort))
        self._sendThread = Thread(target=self.sendThreadStart, args=())
        self._sendThread.start()
        self._logger.logDebug('Started sending')

    def sendThreadStart(self):
        while True:
            item: PriorityQueueItem = self._sendQueue.dequeue()
            self._sendSocket.sendto(item.data, (self._sendIp, self._sendPort))

    def Send(self, buffer: bytes, priority: int):
        self._sendQueue.enqueue(priority=priority, data=buffer)


if __name__ == '__main__':
    logger = ConsoleLogger()
    r = UdpSender(logger, '10.108.102.29', 7800, 7801, 3)
    r.Init()

    while True:
        r.Send(b'12345678', 2)
        logger.logDebug('sent')
        time.sleep(1)
