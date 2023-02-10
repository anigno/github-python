from threading import RLock

class UniqueIdProvider:
    unique_message_id = 1000
    unique_message_id_locker = RLock()

    @staticmethod
    def get_unique_message_id():
        with UniqueIdProvider.unique_message_id_locker:
            UniqueIdProvider.unique_message_id += 1
            return UniqueIdProvider.unique_message_id
