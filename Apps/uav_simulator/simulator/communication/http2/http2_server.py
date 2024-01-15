from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Http2Server:
    def __init__(self, local_ip, local_port):
        self.local_ip = local_ip
        self.local_port = local_port

    def start(self):
        server_address = (self.local_ip, self.local_port)
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.serve_forever()

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Deserialize JSON data to UavStatus object
        json_as_dict = json.loads(post_data)
        print(json_as_dict)
        # uav_status_instance = UavStatus(**uav_status_dict)

        # Send a response (optional)
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    s = Http2Server('localhost', 1000)
    s.start()
