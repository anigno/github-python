import socket
from collections import namedtuple
from threading import Thread
from typing import Optional

from common.generic_event import GenericEvent

BytesReceivedEventArgs = namedtuple('BytesReceivedEventArgs', ['received_data_bytes', 'sender_endpoint_tuple'])

class UdpCommunicator:
    """Sends and receives unicast udp data"""
    UDP_MAX_BUFFER_SEND_SIZE = 65507
    UDP_DEFAULT_RECEIVE_BUFFER_SIZE = 64 * 1024

    def __init__(self, local_ip: str, local_port: int, receive_buffer_size: int = UDP_DEFAULT_RECEIVE_BUFFER_SIZE):
        self._receive_buffer_size = receive_buffer_size
        self._local_port = local_port
        self._local_ip = local_ip
        self._socket: Optional[socket.socket] = None
        self._receiver_thread = Thread(target=self._receiver_thread_start,
                                       name=f'udp_receiver_thread_{local_ip}_{local_port}', daemon=True)
        self.on_data_received = GenericEvent()
        self._init_socket_as_unicast()

    def _init_socket_as_unicast(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self._socket.bind((self._local_ip, self._local_port))

    def _receiver_thread_start(self):
        try:
            while True:
                (received_data_bytes, sender_endpoint_tuple) = self._socket.recvfrom(self._receive_buffer_size)
                self._raise_data_received(received_data_bytes, sender_endpoint_tuple)
        except OSError as ex:
            print(ex)

    def _raise_data_received(self, received_data_bytes, sender_endpoint_tuple):
        event_args = BytesReceivedEventArgs(received_data_bytes, sender_endpoint_tuple)
        self.on_data_received.raise_event(event_args)

    def start_receiving(self):
        self._receiver_thread.start()

    def send_to(self, target_ip, target_port, byte_array: bytes):
        self._socket.sendto(byte_array, (target_ip, target_port))

    def close(self):
        self._socket.close()
