class BytesParser:

    def __init__(self, data_bytes: bytes, start=0):
        self.byte_order = 'big'
        self.data_bytes = data_bytes
        self.i = start

    def get_next_bool(self) -> bool:
        """read next bool value and increment data bytes pointer by 1"""
        b = self.data_bytes[self.i:self.i + 1]
        self.i += 1
        return bool.from_bytes(b, 'big')

    def get_next_uint(self) -> int:
        """read next 32 bit unsigned int value and increment data bytes pointer by 4"""
        b = self.data_bytes[self.i:self.i + 4]
        self.i += 4
        return int.from_bytes(b, 'big', signed=False)

    def get_next_word(self) -> int:
        """read next 16 bit word value and increment data bytes pointer by 2"""
        b = self.data_bytes[self.i:self.i + 2]
        self.i += 2
        return int.from_bytes(b, 'big', signed=False)

    def get_next_int(self) -> int:
        """read next 32-bit signed int value and increment data bytes pointer by 4"""
        b = self.data_bytes[self.i:self.i + 4]
        self.i += 4
        return int.from_bytes(b, 'big', signed=True)

    def get_next_bytes(self, size) -> bytes:
        """read next number of bytes and increment data bytes pointer by that number"""
        b = self.data_bytes[self.i:self.i + size]
        self.i += size
        return b

    @staticmethod
    def to_bytes(uint_num: int, bytes_count: int) -> bytes:
        return uint_num.to_bytes(bytes_count, 'big', signed=False)

    @staticmethod
    def to_uint(data_bytes: bytes, start: int, bytes_count: int):
        i = int.from_bytes(data_bytes[start:start + bytes_count], 'big', signed=False)
        return i

    @staticmethod
    def str_to_bytes(text: str) -> bytes:
        ret = text.encode('utf-8')
        return ret

    @staticmethod
    def str_from_bytes(data_bytes: bytes) -> str:
        ret = data_bytes.decode('utf-8')
        return ret

if __name__ == '__main__':
    v1 = 0xFFFF
    b1 = BytesParser.to_bytes(v1, 2)
    v2 = BytesParser.to_uint(b1, 0, 2)
    assert v1 == v2

    l1 = [0, 1, 2, 3, 4, 5]
    print(l1[2:4])

    a = 'AbCd15'
    d = BytesParser.str_to_bytes(a)
    c = BytesParser.str_from_bytes(d)
    assert a == c
