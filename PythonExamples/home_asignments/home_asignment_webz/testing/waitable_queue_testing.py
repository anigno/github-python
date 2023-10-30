import unittest
from threading import Thread

from PythonExamples.home_asignments.home_asignment_webz.logging.logger import Logger
from PythonExamples.home_asignments.home_asignment_webz.management.waitable_queue import WaitableQueue

class WaitableQueueTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    #TODO: complete test time, assert and exit
    def test_wait_delay(self):
        wq = WaitableQueue(2)
        for a in range(5):
            Logger.log(f'put {a}')
            wq.put(a)

        def get_value(args):
            for _ in range(5):
                v = wq.get()
                Logger.log(f'{args} get {v}')

        Thread(target=get_value, args=[1]).start()
        Thread(target=get_value, args=[2]).start()
