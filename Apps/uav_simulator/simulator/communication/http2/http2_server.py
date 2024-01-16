from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from Apps.uav_simulator.simulator.communication.http2.messages.message_base import MessageBase
from Apps.uav_simulator.simulator.communication.http2.messages_factory import MessagesFactory
from BL.meta_classes.no_instance_meta import NoInstanceMeta
from common.generic_event import GenericEvent

class Http2Server(metaclass=NoInstanceMeta):
    """receive json POST request and raise an event with dict data"""
    on_request_post_received = GenericEvent(MessageBase)

    @staticmethod
    def start(local_ip, local_port):
        server_address = (local_ip, local_port)
        httpd = HTTPServer(server_address, Http2Server.RequestHandler)
        httpd.serve_forever()

    class RequestHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            message_type_value = int.from_bytes(post_data[0:2], 'big', signed=False)
            message = MessagesFactory.create_message_instance(message_type_value)
            Http2Server.on_request_post_received.raise_event(message)
            # Send a response (optional)
            self.send_response(200)
            self.end_headers()

if __name__ == '__main__':
    def on_request_post_received(data_dict: dict):
        print(data_dict)

    MessagesFactory.init()
    Http2Server.on_request_post_received += on_request_post_received
    Http2Server.start('localhost', 1000)
