import crc8
import crcmod

from common.bytes_parser import BytesParser

class CrcUtils:
    CRC8_DIGEST_SIZE = crc8.crc8.digest_size

    @staticmethod
    def calculate_crc8(data_bytes: bytes) -> bytes:
        crc = crc8.crc8()
        crc.update(data_bytes)
        return crc.digest()

    @staticmethod
    def verify_crc8(data_bytes: bytes, crc8_val: bytes) -> bool:
        crc = CrcUtils.calculate_crc8(data_bytes)
        return crc == crc8_val

    @staticmethod
    def calculate_crc32(data_bytes: bytes) -> bytes:
        crc32_func = crcmod.predefined.mkCrcFun('crc-32')
        crc_value = crc32_func(data_bytes)
        data_bytes = BytesParser.to_bytes(crc_value, 4)
        return data_bytes

    @staticmethod
    def verify_crc32(data_bytes: bytes, crc32_val: bytes) -> bool:
        crc_bytes = CrcUtils.calculate_crc32(data_bytes)
        return crc_bytes == crc32_val

if __name__ == '__main__':
    from random import randbytes

    bytes_array1 = randbytes(1024)
    bytes_array2 = bytes_array1 + b'1'
    print(bytes_array1)
    crc_val1 = CrcUtils.calculate_crc8(bytes_array1)
    crc_val2 = CrcUtils.calculate_crc8(bytes_array2)
    assert CrcUtils.verify_crc8(bytes_array1, crc_val1)
    assert not CrcUtils.verify_crc8(bytes_array1, crc_val2)

    crc_val1 = CrcUtils.calculate_crc32(bytes_array1)
    crc_val2 = CrcUtils.calculate_crc32(bytes_array2)
    assert CrcUtils.verify_crc32(bytes_array1, crc_val1)
    assert not CrcUtils.verify_crc32(bytes_array1, crc_val2)
