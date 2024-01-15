import http.client
import json
from http.client import HTTPResponse

from Apps.uav_simulator.simulator.communication.http2.http2_base_type import Http2BaseType

class Http2Client:
    def __init__(self):
        pass

    def send_request(self, instance: Http2BaseType, ip, port, path='/') -> HTTPResponse:
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
            self.age = 32

    c = Http2Client()
    r = c.send_request(SomeData(), 'localhost', 1000)
    print(r.read().decode('utf-8'))
