from ADataSerialization.ASerializerMetaClass import ASerializerMetaClass, binary_type_uint8


class SampleClass(metaclass=ASerializerMetaClass):
    def __init__(self):
        pass

    @binary_type_uint8
    @property
    def PropertyA(self):
        return self._uint8

    @PropertyA.setter
    def PropertyA(self, value):
        self._uint8 = value\

    @binary_type_uint8
    @property
    def PropertyB(self):
        return self._uint8

    @PropertyB.setter
    def PropertyB(self, value):
        self._uint8 = value


if __name__=='__main__':
    sampleClass=SampleClass()
    bf=sampleClass.to_buffer()