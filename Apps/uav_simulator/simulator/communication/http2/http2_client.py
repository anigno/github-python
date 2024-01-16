import http.client
import json
import time
from http.client import HTTPResponse

from Apps.uav_simulator.simulator.communication.http2.messages.message_base import MessageBase, MessageTypeEnum
from Apps.uav_simulator.simulator.communication.http2.messages.status_update_message import StatusUpdateMessage
from BL.meta_classes.no_instance_meta import NoInstanceMeta

class Http2Client(metaclass=NoInstanceMeta):
    """sends http2 dict over json POST request"""

    @staticmethod
    def send_request(message: MessageBase, ip, port) -> HTTPResponse:
        message.send_time = time.time()
        message_bytes = message.to_buffer()
        message_type_bytes = message.MESSAGE_TYPE.value.to_bytes(2, 'big', signed=False)
        body_data = message_type_bytes + message_bytes
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
        conn.request('POST', '/', body=body_data, headers=headers)
        response = conn.getresponse()
        conn.close()
        return response

if __name__ == '__main__':
    message = StatusUpdateMessage()
    r = Http2Client.send_request(message, 'localhost', 1000)
    print(r.read().decode('utf-8'))
