import logging

from Apps.uav_simulator.simulator.logic.simple_uav_manager import SimpleUavManager
from Apps.uav_simulator.testings.simple_uav_manager_config_samples import SimpleUavManagerConfigSamples
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class Runner:
    def __init__(self, uav_params, location, capabilities):
        self.uav = SimpleUavManager(uav_params, location, capabilities)
        self.uav.start()

if __name__ == '__main__':
    from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
    from Apps.uav_simulator.simulator.data_types.location3d import Location3d

    LoggingInitiatorByCode(log_files_path=r'd:\temp\logs\uav1')
    params = UavParams(SimpleUavManagerConfigSamples.config_list[0])
    runner = Runner(params, Location3d(0, 0, 0), [])
    input('Enter to exit')
