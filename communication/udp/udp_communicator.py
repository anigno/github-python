import logging
import socket
import time
from threading import Thread
from typing import Optional

from common.generic_event import GenericEvent
from communication.udp.event_args.data_received_event_args import DataReceivedEventArgs
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class UdpCommunicator:
    """Sends and receives uni-cast udp data"""
    UDP_MAX_BUFFER_SEND_SIZE = 65507
    UDP_DEFAULT_RECEIVE_BUFFER_SIZE = 64 * 1024

    def __init__(self, local_ip: str, local_port: int, receive_buffer_size: int = UDP_DEFAULT_RECEIVE_BUFFER_SIZE):
        logger.debug(f'{local_ip} {local_port}')
        self._local_port = local_port
        self._local_ip = local_ip
        self._receive_buffer_size = receive_buffer_size
        self._is_continue = True
        self._socket: Optional[socket.socket] = None
        self._receiver_thread = None
        self.on_data_received = GenericEvent(DataReceivedEventArgs)
        self.on_error = GenericEvent(Exception)
        self._init_socket_as_unicast()

    def start_receiving(self) -> Thread:
        self._receiver_thread = Thread(target=self._receiver_thread_method,
                                       name=f'udp_receiver_thread_{self._local_ip}_{self._local_port}', daemon=False)
        self._is_continue = True
        self._receiver_thread.start()
        return self._receiver_thread

    def stop_receiving(self):
        self._is_continue = False
        self._socket.close()

    def send_to(self, target_ip, target_port, byte_array: bytes):
        self._socket.sendto(byte_array, (target_ip, target_port))

    def _init_socket_as_unicast(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self._socket.bind((self._local_ip, self._local_port))

    def _receiver_thread_method(self):
        while self._is_continue:
            try:
                (received_data_bytes, sender_endpoint_tuple) = self._socket.recvfrom(self._receive_buffer_size)
                self.handle_data_received(received_data_bytes, sender_endpoint_tuple)
            except OSError as ex:
                if self._is_continue:
                    logger.exception('', exc_info=ex)
                    self.on_error.raise_event(str(ex))
            except Exception as ex:
                logger.exception('', exc_info=ex)
                self.on_error.raise_event(ex)

    def handle_data_received(self, received_data_bytes, sender_endpoint_tuple):
        event_args = DataReceivedEventArgs(received_data_bytes, sender_endpoint_tuple)
        self.on_data_received.raise_event(event_args)

if __name__ == '__main__':
    LoggingInitiatorByCode()
    com1 = UdpCommunicator("127.0.0.1", 1001)
    com1.on_data_received += lambda p: print(p)
    com1.start_receiving()

    com2 = UdpCommunicator("127.0.0.1", 1002)
    com2.on_data_received += lambda p: print(p)
    com2.start_receiving()

    com1.send_to("127.0.0.1", 1002, b"1234567890")
    com2.send_to("127.0.0.1", 1001, b"abcdefghij")

    time.sleep(1)
    logger.debug(f'all sent')
    time.sleep(1)

    com1.stop_receiving()
    com2.stop_receiving()
