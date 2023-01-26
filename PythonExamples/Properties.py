import operator
from random import Random


class Vehicle(object):
    def __init__(self):
        self._color = None
        self._distanceKm = 0
        self._id = Random().randint(1000000, 9999999)

    @property
    def DistanceKm(self) -> int:
        return self._distanceKm

    @DistanceKm.setter
    def DistanceKm(self, value: int):
        self._distanceKm = value

    def _getColor(self):
        return self._color
    def _setColor(self,color:str):
        self._color=color

    Color=property(_getColor,_setColor)



if __name__ == '__main__':
    v = Vehicle()
    v.DistanceKm += 432
    v.DistanceKm += 1497
    print(v.DistanceKm)

    v.Color='White'
    print(v.Color)



