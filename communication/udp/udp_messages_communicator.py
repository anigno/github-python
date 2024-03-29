import logging
import time
from common.crc.crc_providers import CrcProviderBase, CrcProvider32Bit
from common.generic_event import GenericEvent
from communication.udp.event_args.crc_error_event_args import CrcErrorEventArgs
from communication.udp.event_args.data_received_event_args import DataReceivedEventArgs
from communication.udp.event_args.message_received_event_args import MessageReceivedEventArgs
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.serializers.message_serializer_base import MessageSerializerBase
from communication.udp.udp_communicator_with_crc import UdpCommunicatorWithCrc
from communication.udp.udp_message_base import UdpMessageBase
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class UdpMessagesCommunicator:
    """sends and receives messages based of UdpMessageBase, after crc verifications and serialization"""

    def __init__(self, local_ip: str, local_port: int, crc_provider: CrcProviderBase,
                 message_serializer: MessageSerializerBase):
        self.message_serializer = message_serializer
        self.communicator = UdpCommunicatorWithCrc(local_ip, local_port, crc_provider)
        self.communicator.on_data_received += self._on_data_received
        self.communicator.on_crc_error += self._on_crc_error
        self.communicator.on_error += self._on_communicator_error
        self.on_message_received = GenericEvent(MessageReceivedEventArgs)

    def start_receiving(self):
        self.communicator.start_receiving()

    def stop_receiving(self):
        self.communicator.stop_receiving()

    def send_to(self, target_ip: str, target_port: int, message: UdpMessageBase):
        message.sent_time = int(time.time())
        buffer = self.message_serializer.to_buffer(message)
        message_type_bytes = message.MESSAGE_TYPE.to_bytes(length=2, byteorder='big')
        buffer = message_type_bytes + buffer
        self.communicator.send_to(target_ip, target_port, buffer)
        logger.debug(f'sent message_id={message.message_id} to: {target_ip}:{target_port} type={message.MESSAGE_TYPE}')

    def _on_data_received(self, args: DataReceivedEventArgs):
        message_data = MessageReceivedEventArgs()
        message_type_bytes = args.received_data_bytes[0:2]
        message_data.message_type = int.from_bytes(message_type_bytes, byteorder='big')
        data_bytes = args.received_data_bytes[2:]
        message = self.message_serializer.from_buffer(message_data.message_type, data_bytes)
        message_data.message = message
        message_data.sender_endpoint = args.sender_endpoint_tuple
        logger.debug(
            f'received message_id={message.message_id} from: {args.sender_endpoint_tuple} type={message.MESSAGE_TYPE}')
        self.on_message_received.raise_event(message_data)

    def _on_crc_error(self, args: CrcErrorEventArgs):
        logger.warning(f'crc error, sender:{args.sender_endpoint_tuple}')

    def _on_communicator_error(self, ex: Exception):
        logger.exception('', exc_info=ex)

if __name__ == '__main__':
    LoggingInitiatorByCode()

    class MessageSample(UdpMessageBase):
        MESSAGE_TYPE = 1234

        def __init__(self):
            super().__init__()
            self.a = 123
            self.b = 'abcdefg'
            self.c = [1, 2, 3]

        def __str__(self):
            return f'{self.a} {self.b} {self.c}'

    def on_message_received(args: MessageReceivedEventArgs):
        logger.debug(f'* on_message_received {args.message}')

    comm1 = UdpMessagesCommunicator('127.0.0.1', 1001, CrcProvider32Bit(), PickleMessageSerializer())
    comm1.start_receiving()
    comm2 = UdpMessagesCommunicator('127.0.0.1', 1002, CrcProvider32Bit(), PickleMessageSerializer())
    comm2.start_receiving()
    comm1.on_message_received += on_message_received
    comm2.on_message_received += on_message_received
    comm1.send_to('127.0.0.1', 1002, MessageSample())
    comm2.send_to('127.0.0.1', 1001, MessageSample())
    time.sleep(1)
    comm1.stop_receiving()
    comm2.stop_receiving()
