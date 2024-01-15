import http.client
import json
from http.client import HTTPResponse

from Apps.uav_simulator.simulator.communication.http2.http2_base_type import Http2BaseType
from BL.meta_classes.no_instance_meta import NoInstanceMeta

class Http2Client(metaclass=NoInstanceMeta):
    @staticmethod
    def send_request(instance: Http2BaseType, ip, port, path='/') -> HTTPResponse:
        as_json = json.dumps(instance.__dict__)
        conn = http.client.HTTPConnection(ip, port)
        headers = {
            'Content-Type': 'application/json',
            'Connection': 'Upgrade',
            'Upgrade': 'h2c',
        }
        conn.request('POST', path, body=as_json, headers=headers)
        response = conn.getresponse()
        conn.close()
        return response

if __name__ == '__main__':
    class SomeData:
        def __init__(self):
            self.name = 'abc'
            self.data = [1, 2, 3]

    r = Http2Client.send_request(SomeData(), 'localhost', 1000)
    print(r.read().decode('utf-8'))
