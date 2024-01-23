import os

from Apps.uav_simulator.simulator.capabilities.capability_base import CapabilityBase
from Apps.uav_simulator.simulator.capabilities.capability_data import CapabilityData
from Apps.uav_simulator.simulator.data_types.uav_status import UavStatus

class CameraSimulationCapability(CapabilityBase):
    def __init__(self):

    def get(self, uav_status: UavStatus) -> CapabilityData:
        image_bytes = b''
        return CapabilityData('CAMERA01_JPG', image_bytes)

if __name__ == '__main__':
    from PIL import Image
    import io

    print(os.getcwd())
    image_path = r'..\..\testings\house.jpg'
    image = Image.open(image_path)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='JPEG')
    image_bytes = image_bytes.getvalue()
    image.close()
