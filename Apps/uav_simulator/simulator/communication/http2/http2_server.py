from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from BL.meta_classes.no_instance_meta import NoInstanceMeta
from common.generic_event import GenericEvent

class Http2Server(metaclass=NoInstanceMeta):
    """receive json POST request and raise an event with dict data"""
    on_request_post_received = GenericEvent(dict)

    @staticmethod
    def start(local_ip, local_port):
        server_address = (local_ip, local_port)
        httpd = HTTPServer(server_address, Http2Server.RequestHandler)
        httpd.serve_forever()

    class RequestHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            json_as_dict = json.loads(post_data)
            Http2Server.on_request_post_received.raise_event(json_as_dict)
            # Send a response (optional)
            self.send_response(200)
            self.end_headers()

if __name__ == '__main__':
    def on_request_post_received(data_dict: dict):
        # uav_status_instance = UavStatus(**uav_status_dict)
        print(data_dict)
    Http2Server.on_request_post_received += on_request_post_received
    Http2Server.start('localhost', 1000)
