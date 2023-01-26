import socket

udp_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sender.bind('10.108.102.29',)
