import logging
from typing import List

from Apps.uav_simulator.simulator.data_types.location3d import Location3d
from Apps.uav_simulator.simulator.data_types.uav_params import UavParams
from Apps.uav_simulator.simulator.messages.fly_to_destination_message import FlyToDestinationMessage
from Apps.uav_simulator.simulator.messages.ground_control_update_message import GroundControlUpdateMessage
from Apps.uav_simulator.simulator.messages.return_to_home_message import ReturnToHomeMessage
from Apps.uav_simulator.testings.simple_uav_manager_config_samples import SimpleUavManagerConfigSamples
from common.crc.crc_providers import CrcProvider32Bit
from communication.udp.event_args.message_received_event_args import MessageReceivedEventArgs
from communication.udp.serializers.pickle_message_serializer import PickleMessageSerializer
from communication.udp.udp_messages_communicator import UdpMessagesCommunicator
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class GroundControlMock:
    def __init__(self, uav_list: List[UavParams]):
        self.communicator = UdpMessagesCommunicator('127.0.0.1', 1000, CrcProvider32Bit(), PickleMessageSerializer())
        self.communicator.on_message_received += self.on_message_received
        self.uav_list = uav_list
        self.home_location = Location3d(0, 0, 0)

    def start(self):
        self.communicator.start_receiving()

    def fly_to(self, selected_uav_params: UavParams, location):
        self.communicator.send_to(selected_uav_params.uav_ip, selected_uav_params.uav_port,
                                  FlyToDestinationMessage(location))

    def return_home(self, selected_uav_params: UavParams):
        self.communicator.send_to(selected_uav_params.uav_ip, selected_uav_params.uav_port,
                                  ReturnToHomeMessage(self.home_location))

    def on_message_received(self, args: MessageReceivedEventArgs):
        if args.message_type == GroundControlUpdateMessage.MESSAGE_TYPE:
            message: GroundControlUpdateMessage = args.message
            logger.debug(
                f'{message.uav_name} {message.uav_status.flight_mode} {message.uav_status.location}'
                f' {message.uav_status.remaining_flight_time}')

if __name__ == '__main__':
    import time

    LoggingInitiatorByCode(log_files_path=r'd:\temp\logs\gc')

    uav_params_list = [UavParams(params) for params in SimpleUavManagerConfigSamples.config_list]

    gcm = GroundControlMock(uav_params_list)
    gcm.start()
    time.sleep(2)
    while True:
        gcm.fly_to(uav_params_list[0], Location3d(100, 100, 100))
        time.sleep(3)
