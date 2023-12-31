import logging
import time
from threading import RLock
from common.crc.crc_providers import CrcProviderBase, CrcProvider32Bit
from common.generic_event import GenericEvent
from communication.udp.crc_error_event_args import CrcErrorEventArgs
from communication.udp.data_received_event_args import DataReceivedEventArgs
from communication.udp.message_base import MessageBase
from communication.udp.message_data import MessageData
from communication.udp.udp_communicator import UdpCommunicator
from communication.udp.udp_communicator_with_crc import UdpCommunicatorWithCrc
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class UdpMessagesCommunicator:
    """sends and received messages based of MessageBase, after crc verifications"""

    def __init__(self, local_ip: str, local_port: int, crc_provider: CrcProviderBase,
                 receive_buffer_size=UdpCommunicator.UDP_DEFAULT_RECEIVE_BUFFER_SIZE):
        self.communicator = UdpCommunicatorWithCrc(local_ip, local_port, crc_provider, receive_buffer_size)
        self.communicator.on_data_received += self.on_data_received
        self.communicator.on_crc_error += self.on_crc_error
        self.on_message_received = GenericEvent(MessageData)
        self.statistics_locker = RLock()

    def start_receiving(self):
        self.communicator.start_receiving()

    def stop_receiving(self):
        self.communicator.stop_receiving()

    def send_to(self, target_ip, target_port, message: MessageBase):
        buffer = message.to_buffer()
        message_type_bytes = message.MESSAGE_TYPE.to_bytes(length=2, byteorder='big')
        buffer = message_type_bytes + buffer
        self.communicator.send_to(target_ip, target_port, buffer)

    def on_data_received(self, args: DataReceivedEventArgs):
        message_data = MessageData()
        message_type_bytes = args.received_data_bytes[0:2]
        message_data.message_type = int.from_bytes(message_type_bytes, byteorder='big')
        message_data.data_bytes = args.received_data_bytes[2:]
        message_data.sender_endpoint = args.sender_endpoint_tuple
        self.on_message_received.raise_event(message_data)

    def on_crc_error(self, args: CrcErrorEventArgs):
        logger.warning(f'crc error, sender:{args.sender_endpoint_tuple}')

if __name__ == '__main__':
    class MessageSample(MessageBase):
        MESSAGE_TYPE = 1234

        def __init__(self):
            self.a = 123
            self.b = 'abcdefg'
            self.c = [1, 2, 3]

        def __str__(self):
            return f'{self.a} {self.b} {self.c}'

    def on_message_received(args: MessageData):
        message = MessageBase.from_buffer(args.data_bytes)
        print(message)

    comm1 = UdpMessagesCommunicator('127.0.0.1', 1001, CrcProvider32Bit())
    comm1.start_receiving()
    comm2 = UdpMessagesCommunicator('127.0.0.1', 1002, CrcProvider32Bit())
    comm2.start_receiving()
    comm1.on_message_received += on_message_received
    comm2.on_message_received += on_message_received
    comm1.send_to('127.0.0.1', 1002, MessageSample())
    comm2.send_to('127.0.0.1', 1001, MessageSample())
    time.sleep(1)
    comm1.stop_receiving()
    comm2.stop_receiving()
