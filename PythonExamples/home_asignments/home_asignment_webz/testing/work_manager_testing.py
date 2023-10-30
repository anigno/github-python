import unittest

from PythonExamples.home_asignments.home_asignment_webz.management.work_manager import WorkManager
from PythonExamples.home_asignments.home_asignment_webz.workers.worker_base import WorkerBase

class WorkManagerTesting(unittest.TestCase):

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

    def test_workers_creation(self):
        # prepare
        work_manager_config = {"worker_name_prefix": "worker_", "number_of_workers": 5}
        # run
        work_manager = WorkManager(work_manager_config_dict=work_manager_config,
                                   worker_thread_type=DammyWorker)
        # test
        self.assertEqual(len(work_manager._workers), 5)

class DammyWorker(WorkerBase):
    def target_method(self):
        pass
