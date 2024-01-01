import time
import logging
from common.generic_event import GenericEvent
from communication.udp.event_args.crc_error_event_args import CrcErrorEventArgs
from common.crc.crc_providers import CrcProviderBase, CrcProvider32Bit
from communication.udp.udp_communicator import UdpCommunicator
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class UdpCommunicatorWithCrc(UdpCommunicator):

    def __init__(self, local_ip: str, local_port: int, crc_provider: CrcProviderBase,
                 receive_buffer_size=UdpCommunicator.UDP_DEFAULT_RECEIVE_BUFFER_SIZE):
        super().__init__(local_ip, local_port, receive_buffer_size)
        self.crc_provider = crc_provider
        self.on_crc_error = GenericEvent(CrcErrorEventArgs)

    def send_to(self, target_ip, target_port, byte_array: bytes):
        byte_array_with_crc = self.crc_provider.add_crc(byte_array)
        super().send_to(target_ip, target_port, byte_array_with_crc)

    def handle_data_received(self, received_crc_and_data_bytes, sender_endpoint_tuple):
        """strip and verify the crc part, call super to handle data event"""
        crc_verification_result = self.crc_provider.verify_crc(received_crc_and_data_bytes)
        if crc_verification_result.is_crc_ok:
            super().handle_data_received(crc_verification_result.byte_array, sender_endpoint_tuple)
        else:
            event_args = CrcErrorEventArgs(sender_endpoint_tuple=sender_endpoint_tuple)
            self.on_crc_error.raise_event(event_args)

if __name__ == '__main__':
    LoggingInitiatorByCode()
    com1 = UdpCommunicatorWithCrc("127.0.0.1", 1001, CrcProvider32Bit())
    com1.on_data_received += lambda p: print(p)
    com1.on_crc_error += lambda p: print(p)
    com1.start_receiving()

    com2 = UdpCommunicatorWithCrc("127.0.0.1", 1002, CrcProvider32Bit())
    com2.on_data_received += lambda p: print(p)
    com2.on_crc_error += lambda p: print(p)
    com2.start_receiving()

    logger.debug(f'sending two messages from each communicator')
    com1.send_to("127.0.0.1", 1002, b"1234567890")
    com2.send_to("127.0.0.1", 1001, b"abcdefghij")

    time.sleep(1)
    logger.debug(f'sent')

    com1.stop_receiving()
    com2.stop_receiving()
