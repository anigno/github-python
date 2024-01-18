import http.client
from http.client import HTTPResponse

from BL.meta_classes.no_instance_meta import NoInstanceMeta

class Http2Client(metaclass=NoInstanceMeta):
    """sends data bytes over http2 POST request"""

    @staticmethod
    def send_data_request(data: bytes, ip, port) -> HTTPResponse:
        conn = http.client.HTTPConnection(ip, port)
        # for json content
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Connection': 'Upgrade',
        #     'Upgrade': 'h2c',
        # }
        # for binary content
        headers = {
            'Content-Type': 'application/octet-stream',
            'Connection': 'Upgrade',
            'Upgrade': 'h2c',
        }
        conn.request('POST', '/', body=data, headers=headers)
        response = conn.getresponse()
        conn.close()
        return response

if __name__ == '__main__':
    # message1 = StatusUpdateMessage()
    data = b'12345678'
    r = Http2Client.send_data_request(data, 'localhost', 1000)
    print(r.read().decode('utf-8'))
