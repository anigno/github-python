from enum import Enum

class SelectedSound(Enum):
    NONE = 0
    CONSTRUCTION = 1
    DOGS = 2
    FREQUENCIES = 3
    MUSIC = 4

class PlayingMode(Enum):
    STOPPED = 0
    PLAYING = 1
    TRIGGERED = 2

