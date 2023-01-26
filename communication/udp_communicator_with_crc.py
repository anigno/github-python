from collections import namedtuple
from common.generic_event import GenericEvent
from communication.crc_providers import CrcProvider8Bit, CrcProviderBase
from communication.udp_communicator import UdpCommunicator

CrcErrorEventArgs = namedtuple('CrcErrorEventArgs', ['sender_endpoint_tuple'])

class UdpCommunicatorWithCrc(UdpCommunicator):

    def __init__(self, local_ip: str, local_port: int, crc_provider: CrcProviderBase,
                 receive_buffer_size=UdpCommunicator.UDP_DEFAULT_RECEIVE_BUFFER_SIZE):
        super().__init__(local_ip, local_port, receive_buffer_size)
        self.crc_provider = crc_provider
        self.on_crc_error = GenericEvent()

    def send_to(self, target_ip, target_port, byte_array: bytes):
        byte_array = self.crc_provider.add_crc(byte_array)
        super().send_to(target_ip, target_port, byte_array)

    def _data_received_handling(self, received_crc_and_data_bytes, sender_endpoint_tuple):
        crc_result = self.crc_provider.verify_crc(received_crc_and_data_bytes)
        if crc_result.is_crc_ok:
            super()._data_received_handling(crc_result.byte_array, sender_endpoint_tuple)
        else:
            event_args = CrcErrorEventArgs(sender_endpoint_tuple=sender_endpoint_tuple)
            self.on_crc_error.raise_event(event_args)


if __name__ == '__main__':
    com1 = UdpCommunicatorWithCrc('127.0.0.1', 5000, CrcProvider8Bit())
    a = b'12345678' * 1024
