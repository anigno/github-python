import logging
import time
from queue import Queue
from common.crc.crc_providers import CrcProvider32Bit, CrcProviderBase
from communication.udp.event_args.message_data_event_args import MessageDataEventArgs
from communication.udp.message_base import MessageBase
from communication.udp.serializers.message_serializer_base import MessageSerializerBase
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.udp_messages_communicator import UdpMessagesCommunicator
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class UdpCommunicationManager:
    """sends messages and queue received messages"""

    def __init__(self, local_ip: str, local_port: int, crc_provider: CrcProviderBase,
                 message_serializer: MessageSerializerBase):
        self.communicator = UdpMessagesCommunicator(local_ip, local_port, crc_provider, message_serializer)
        self.communicator.on_message_received += self._on_message_received
        self.received_messages_queue: Queue[MessageDataEventArgs] = Queue()

    def send_to(self, target_ip: str, target_port: int, message: MessageBase):
        self.communicator.send_to(target_ip, target_port, message)

    def dequeue_received_message(self):
        return self.received_messages_queue.get()

    def receive_messaged_queue_size(self):
        return self.received_messages_queue.qsize()

    def start_receiving(self):
        self.communicator.start_receiving()

    def stop_receiving(self):
        self.communicator.stop_receiving()

    def _on_message_received(self, args: MessageDataEventArgs):
        self.received_messages_queue.put(args)

if __name__ == '__main__':
    LoggingInitiatorByCode()

    class Message1(MessageBase):
        MESSAGE_TYPE = 111

        def __init__(self, n):
            self.n = n
            self.b = 'abc'

        def __str__(self):
            return f'{self.n} {self.b}'

    class Message2(MessageBase):
        MESSAGE_TYPE = 222

        def __init__(self, n):
            self.n = n
            self.c = [1, 2, 3]
            self.d = {1: '111', 2: '222'}

        def __str__(self):
            return f'{self.n} {self.c} {self.d}'

    comm1 = UdpCommunicationManager('127.0.0.1', 1001, CrcProvider32Bit(), PickleMessageSerializer())
    comm1.start_receiving()
    comm2 = UdpCommunicationManager('127.0.0.1', 1002, CrcProvider32Bit(), PickleMessageSerializer())
    comm2.start_receiving()
    for a in range(5):
        comm1.send_to('127.0.0.1', 1002, Message1(a))
        comm1.send_to('127.0.0.1', 1002, Message2(a + 10))
    time.sleep(1)
    logger.debug(f'queue size={comm2.receive_messaged_queue_size()}')
    for _ in range(10):
        args = comm2.dequeue_received_message()
        logger.debug(f'{args.message_type} {args.sender_endpoint} {args.message}')
    logger.debug(f'queue size={comm2.receive_messaged_queue_size()}')

    comm1.stop_receiving()
    comm2.stop_receiving()
