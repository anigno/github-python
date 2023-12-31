from abc import ABC, abstractmethod
from collections import namedtuple

from common.bytes_parser import BytesParser
from common.crc.crc_utils import CrcUtils

CrcVerificationResult = namedtuple('CrcVerificationResult', ['is_crc_ok', 'byte_array'])

class CrcProviderBase(ABC):
    @abstractmethod
    def add_crc(self, byte_array: bytes) -> bytes:
        pass

    @abstractmethod
    def verify_crc(self, crc_and_byte_array: bytes) -> CrcVerificationResult:
        pass

class CrcProvider8Bit(CrcProviderBase):
    def add_crc(self, byte_array: bytes) -> bytes:
        return CrcUtils.calculate_crc8(byte_array) + byte_array

    def verify_crc(self, crc_and_byte_array: bytes) -> CrcVerificationResult:
        received_crc8 = BytesParser.to_bytes(crc_and_byte_array[0], 1)
        received_data_bytes = crc_and_byte_array[1:]
        calculate_crc8 = CrcUtils.calculate_crc8(received_data_bytes)
        return CrcVerificationResult(received_crc8 == calculate_crc8, received_data_bytes)

class CrcProvider32Bit(CrcProviderBase):
    def add_crc(self, byte_array: bytes) -> bytes:
        return CrcUtils.calculate_crc32(byte_array) + byte_array

    def verify_crc(self, crc_and_byte_array: bytes) -> CrcVerificationResult:
        received_crc32 = crc_and_byte_array[0:4]
        received_data_bytes = crc_and_byte_array[4:]
        calculated_crc32 = CrcUtils.calculate_crc32(received_data_bytes)
        return CrcVerificationResult(received_crc32 == calculated_crc32, received_data_bytes)

if __name__ == '__main__':
    cp = CrcProvider32Bit()
    crc_and_data = cp.add_crc(b'12345678')
    cr = cp.verify_crc(crc_and_data)
    print(f'{cr}')
    assert cr.is_crc_ok
    cr = cp.verify_crc(b'eeee' + b'12345678')
    print(f'{cr}')
    assert not cr.is_crc_ok

    cp = CrcProvider8Bit()
    crc_and_data = cp.add_crc(b'12345678')
    cr = cp.verify_crc(crc_and_data)
    print(f'{cr}')
    assert cr.is_crc_ok
    cr = cp.verify_crc(b'e' + b'12345678')
    print(f'{cr}')
    assert not cr.is_crc_ok
