from enum import Enum

class SelectedSound(Enum):
    NONE = 0
    CONSTRUCTION = 1
    DOGS = 2
    FREQUENCIES = 3
    MUSIC1 = 4
    MUSIC2 = 5
    MUSIC3 = 6

class PlayingMode(Enum):
    STOPPED = 0
    PLAYING = 1
    TRIGGERED = 2

