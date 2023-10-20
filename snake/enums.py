from enum import Enum

class Rotation(Enum):
    Forward = 1
    Backward = -1
    Right = 1
    Left = -1

    def __call__(self):
        return self.value
