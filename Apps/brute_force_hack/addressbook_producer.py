import os
import platform
from pprint import pprint

from wifi_utils import get_wifi_networks
class AddressBookProducer:
    def generate_by_phone_number(self) -> int:
        # 05########
        for a in range(9999999):
            yield f'05{a}'

    
if __name__ == '__main__':
    a = AddressBookProducer()
    pprint(get_wifi_networks())

