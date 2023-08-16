from threading import Semaphore

class ReadersWritesLocker:
    def __init__(self):
        self.reader_semaphore = Semaphore(1)
        self.writer_semaphore = Semaphore(1)
        self.readers = 0

    def reader_lock(self):
        self.reader_semaphore.acquire()
        self.readers += 1
        if self.readers == 1:
            self.writer_semaphore.acquire()
        self.reader_semaphore.release()

    def reader_unlock(self):
        self.reader_semaphore.acquire()
        self.readers -= 1
        if self.readers == 0:
            self.writer_semaphore.release()
        self.reader_semaphore.release()

    def writer_lock(self):
        self.writer_semaphore.acquire()

    def writer_unlock(self):
        self.writer_semaphore.release()

if __name__ == '__main__':
