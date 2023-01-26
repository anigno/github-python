import socket
from threading import Thread

from Communication.Udp.LoggerBase import LoggerBase
from Communication.Udp.ConsoleLogger import ConsoleLogger


class UdpReceiver:
    """
    message structure:
        [crc(B)][counter(B)][part(B)][parts(B)][data(0-16M)]
    """

    def __init__(self, logger: LoggerBase, receiveIp: str, receivePort: int):
        self._logger = logger
        self._receivePort = receivePort
        self._receiveIp = receiveIp
        self._receiveBufferSize = 1024
        self._receiveSocket = None
        self._listenThread = None

    def Init(self):
        self._receiveSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._receiveSocket.bind((self._receiveIp, self._receivePort))
        self._listenThread = Thread(target=self.listenThreadStart, args=())
        self._listenThread.start()
        self._logger.logDebug('Started listening')

    def listenThreadStart(self):
        while True:
            byteAddressPair = self._receiveSocket.recvfrom(self._receiveBufferSize)
            message = byteAddressPair[0]
            senderAddress = byteAddressPair[1]
            crc = message[0]
            counter = message[1]
            part = message[2]
            parts = message[3]
            message = message[4:]
            self._logger.logDebug(f'{senderAddress} crc{crc} cnt{counter} part{part} parts{parts} message[{message}]')


if __name__ == '__main__':
    logger = ConsoleLogger()
    r = UdpReceiver(logger, '10.108.102.29', 7800)
    r.Init()
