import time
import unittest

from communication.crc_providers import CrcProviderBase, CrcVerificationResult
from communication.udp_communicator import BytesReceivedEventArgs
from communication.udp_communicator_with_crc import CrcErrorEventArgs, UdpCommunicatorWithCrc

class CrcProviderMock(CrcProviderBase):
    def __init__(self):
        self.cnt = 0

    def add_crc(self, byte_array: bytes) -> bytes:
        return byte_array

    def verify_crc(self, crc_and_byte_array: bytes) -> CrcVerificationResult:
        self.cnt += 1
        return CrcVerificationResult(self.cnt <= 1, crc_and_byte_array)


class TestUdpCommunicator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data_8k = 1024 * b'12345678'
        self.receive_counter = 0
        self.crc_error_counter = 0

    def event_handler(self, event_args: BytesReceivedEventArgs):
        print(f'received from: {event_args.sender_endpoint_tuple} '
              f'data of length: {len(event_args.received_data_bytes)}')
        self.assertEqual(event_args.received_data_bytes, self.test_data_8k)
        self.receive_counter += 1

    def crc_error_event_handler(self, event_args: CrcErrorEventArgs):
        print(f'crc error {event_args}')
        self.crc_error_counter += 1

    def test_send_receive_crc_calls(self):
        crc_mock = CrcProviderMock()
        com1 = UdpCommunicatorWithCrc('127.0.0.1', 1001, crc_mock)
        com2 = UdpCommunicatorWithCrc('127.0.0.2', 1002, crc_mock)

        com1.on_data_received += self.event_handler
        com1.on_crc_error += self.crc_error_event_handler
        com2.on_data_received += self.event_handler
        com2.on_crc_error += self.crc_error_event_handler

        com1.start_receiving()
        com2.start_receiving()

        time.sleep(1)
        com2.send_to('127.0.0.1', 1001, self.test_data_8k)
        time.sleep(0.1)
        com1.send_to('127.0.0.2', 1002, self.test_data_8k)

        time.sleep(1)
        self.assertEqual(self.receive_counter, 1)
        self.assertEqual(self.crc_error_counter, 1)
        com1.close()
        com2.close()
        print('end')
