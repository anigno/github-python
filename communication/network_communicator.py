class NetworkCommunicator:
    unique_message_id = 1000

    @staticmethod
    def get_unique_message_id():
        NetworkCommunicator.unique_message_id += 1
        return NetworkCommunicator.unique_message_id

    def __init__(self):
        pass