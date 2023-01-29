from common.time_utils import TimeUtils

class Partition:
    """
    describe one of many parts of a message data bytes
    """

    def __init__(self, index: int, data_bytes: bytes, receive_timeout_interval: int):
        """
        @param index: index of the part
        @param data_bytes: the data bytes of the part
        @param receive_timeout_interval: interval to wait for ack for this part
        """
        self.index = index
        self.data_bytes = data_bytes


    def __repr__(self):
        return f'[Partition: {self.index},{self.data_bytes}]'
