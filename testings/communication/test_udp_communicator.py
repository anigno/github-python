import time
import unittest

from communication.udp.udp_communicator import UdpCommunicator
from communication.udp.data_received_event_args import DataReceivedEventArgs

class TestUdpCommunicator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_data_8k = 1024 * b'12345678'
        self.receive_counter = 0

    def event_handler(self, event_args: DataReceivedEventArgs):
        print(f'{self.receive_counter} received from: {event_args.sender_endpoint_tuple} '
              f'data of length: {len(event_args.received_data_bytes)}')
        self.assertEqual(event_args.received_data_bytes, self.test_data_8k)
        self.receive_counter += 1

    def test_send_receive_data_correct(self):
        com1 = UdpCommunicator('127.0.0.1', 1001)
        com2 = UdpCommunicator('127.0.0.2', 1002)

        com1.on_data_received += self.event_handler
        com2.on_data_received += self.event_handler
        com1.start_receiving()
        com2.start_receiving()

        time.sleep(0.1)
        com2.send_to('127.0.0.1', 1001, self.test_data_8k)
        time.sleep(0.1)
        com1.send_to('127.0.0.2', 1002, self.test_data_8k)

        time.sleep(0.1)
        self.assertEqual(self.receive_counter, 2)
        time.sleep(1)

        # com1.close()
        # com2.close()
        print('end')


