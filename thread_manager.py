import threading
import time
from threading import Thread
from typing import List
class ThreadManager:
    MAX_CNT = 31536000  # 24*3600*365 one year in seconds

    def __init__(self):
        self._dix_state_persistence = dix_state_persistence
        self._db_sync_manager = db_sync_manager
        self.iteration_modules_provider = iteration_modules_provider
        self._logger = logging.getLogger(f'{LoggerNames.dix.name}.{LoggerSections.status.name}')
        self._permission_checker: PermissionCheckerBase = permission_checker
        self._data_model = data_model
        self._sd_service = sd_service
        self._discovery_manager: DiscoveryManager = discovery_manager
        self._client_communication_manager: ClientCommunicationManager = client_communication_manager
        self._network_communication_manager: NetworkCommunicationManager = network_communication_manager
        self._executor_manager: IExecutorManager = executor_manager
        self._reports_manager = reports_manager
        self._threads_frequency_config: ThreadFrequencyConfig = threads_frequency_config
        self._threadLocker = threading.Event()
        self._threadCounter = {}  # A dictionary holding iteration call counters, from each running thread. used for fairness monitoring
        self._iterationModulesThreadN: List[IIterationModule] = iteration_modules_provider.iteration_modules
        self._permission_checker.on_access.subscribe(self.on_permission_access)
        self._permission_checker.on_denied.subscribe(self.on_permission_denied)
        self.capability_connectivity_updater = capability_connectivity_updater
        self.capability_connectivity_updater.start()

    def start(self):
        self.main_loop()

    def main_loop(self):
        threads = []

        # init network communication
        network_thread_high = Thread(target=self.thread_network_high_priority, name='DixHigh', args=[])
        network_thread_high.start()
        threads.append(network_thread_high)
        network_thread_low = Thread(target=self.thread_network_low_priority, name='DixLow', args=[])
        network_thread_low.start()
        threads.append(network_thread_low)

        # init other threads
        monitoring_thread = Thread(target=self.thread_monitoring, name='Monitoring', args=[self._threads_frequency_config.monitoring_thread_interval])
        monitoring_thread.start()
        threads.append(monitoring_thread)
        sd_thread = Thread(target=self.thread_sd, name='SD', args=[self._threads_frequency_config.sd_thread_interval])
        sd_thread.start()
        threads.append(sd_thread)
        report_thread = Thread(target=self.thread_client_report, name='R', args=[self._threads_frequency_config.client_report_thread_interval])
        report_thread.start()
        threads.append(report_thread)
        n_thread = Thread(target=self.thread_n, name='N', args=[self._threads_frequency_config.n_thread_base_interval])
        n_thread.start()
        threads.append(n_thread)
        db_thread = Thread(target=self.thread_database, name='Db', args=[self._threads_frequency_config.database_sync_thread_interval])
        db_thread.start()
        threads.append(db_thread)

        for thread in threads:
            thread.join()

    # region thread functions
    def thread_sd(self, interval: float):
        self._logger.debug(f'[thread_manager] Start SD thread. Repeat interval={interval}')
        while True:
            self._threadLocker.clear()
            t0 = time.time()
            self.iteration_count()
            try:
                self._sd_service.process_iteration()
            except Exception as ex:
                self._logger.exception(f'[thread_manager] {ex.args}')
            self._threadLocker.set()
            self.sleep_delta(t0, interval)

    def thread_network_high_priority(self):  # using blocking queue. sleep is not needed.
        self._logger.debug(f'[thread_manager] Start network high priority thread. ')
        while True:
            self._threadLocker.wait()
            self.iteration_count()
            try:
                self._executor_manager.network_high_priority_queue_iteration()
            except Exception as ex:
                self._logger.exception(str(ex))

    def thread_network_low_priority(self):  # using blocking queue. sleep is not needed.
        self._logger.debug(f'[thread_manager] Start network low priority thread. ')
        while True:
            self._threadLocker.wait()
            self.iteration_count()
            try:
                self._executor_manager.network_low_priority_queue_iteration()
            except Exception as ex:
                self._logger.exception(str(ex))

    def thread_database(self, db_sync_interval: float):
        self._logger.debug(f'[thread_manager] Start database sync thread. Repeat interval={db_sync_interval}')
        # cnt: int = 0
        # factor: int = int((data_model_save_interval // db_sync_interval) + ((data_model_save_interval / db_sync_interval) > 0))
        # self._logger.debug(f'[thread_manager] Start database sync thread. Repeat factor={factor}')
        while True:
            t0 = time.time()
            self.iteration_count()
            try:
                self._data_model.save()
                self._dix_state_persistence.save()
            except Exception as ex:
                self._logger.exception(str(ex))
            self.sleep_delta(t0, db_sync_interval)
            # cnt -= 1

    def thread_client_report(self, interval: float):
        self._logger.debug(f'[thread_manager] Start client report thread. Repeat interval={interval}')
        while True:
            t0 = time.time()
            self.iteration_count()
            try:
                self._reports_manager.process_iteration()
                pass
            except Exception as ex:
                self._logger.exception(str(ex))
            self.sleep_delta(t0, interval)

    def thread_n(self, interval: float):
        self._logger.debug(f'[thread_manager] Start N thread. Repeat interval={interval}')
        cnt = 0
        while True:
            t0 = time.time()
            self.iteration_count()
            try:
                cnt += 1
                for iteration_module in self._iterationModulesThreadN:
                    if cnt % iteration_module.frequency == 0:
                        iteration_module.process_iteration()
            except Exception as ex:
                self._logger.exception(str(ex))
            self.sleep_delta(t0, interval)

    def thread_monitoring(self, interval: float):
        self._logger.debug(f'[thread_monitoring] Start monitoring thread. Repeat interval={interval}')

        while True:
            time.sleep(interval)
            running_time = time.process_time()
            for key in self._threadCounter.keys():
                self._logger.info(f'[thread_monitoring] ********** {key} cnt={self._threadCounter[key]} iterTime={round(running_time / self._threadCounter[key], 3)}')

    # endregion tread functions

    # region help functions
    def sleep_delta(self, t0: float, interval: float):
        """
        Sleep remaining time between requested interval and time passed from given t0
        :param t0: time.time() of starting measurement
        :param interval: total time including activity
        """
        t1 = time.time()
        dt = t1 - t0
        sleep_time = interval - dt
        if sleep_time < 0:
            self._logger.warning(f'[thread_manager] Timeout in: {threading.currentThread().name} {sleep_time}')
            sleep_time = 0
        time.sleep(sleep_time)

    def iteration_count(self):
        """
        Increase iteration count for current thread, used for monitoring fairness
        """
        thread_name = threading.current_thread().name
        self._threadCounter[thread_name] = self._threadCounter.get(thread_name, 0) + 1
    # endregion help functions
