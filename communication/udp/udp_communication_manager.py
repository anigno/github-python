from queue import Queue

from common.crc.crc_providers import CrcProvider32Bit
from communication.udp.event_args.message_data_event_args import MessageDataEventArgs
from communication.udp.message_base import MessageBase
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.udp_messages_communicator import UdpMessagesCommunicator

class UdpCommunicationManager:
    """sends messages and queue received messages"""

    def __init__(self, local_ip, local_port, crc_provider, message_serializer, receive_message_size):
        self.communicator = UdpMessagesCommunicator(local_ip, local_port, crc_provider, message_serializer,
                                                    receive_message_size)
        self.communicator.on_message_received += self._on_message_received
        self.received_messages_queue = Queue()

    def send_to(self, target_ip: str, target_port: int, message: MessageBase):
        self.communicator.send_to(target_ip, target_port, message)

    def dequeue_message(self):
        return self.received_messages_queue.get()

    def start_receiving(self):
        self.communicator.start_receiving()

    def stop_receiving(self):
        self.communicator.stop_receiving()

    def _on_message_received(self, args: MessageDataEventArgs):
        self.received_messages_queue.put(args)

if __name__ == '__main__':
    class Message1(MessageBase):
        def __init__(self):
            self.a = 123
            self.b = 'abc'

    class Message2(MessageBase):
        def __init__(self):
            self.c = [1, 2, 3]
            self.d = {1: '111', 2: '222'}

    comm1 = UdpCommunicationManager('127.0.0.1', 1001, CrcProvider32Bit(), PickleMessageSerializer())
    comm1.start_receiving()
    comm2 = UdpCommunicationManager('127.0.0.1', 1002, CrcProvider32Bit(), PickleMessageSerializer())
    comm2.start_receiving()

