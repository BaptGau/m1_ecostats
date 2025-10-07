from enum import Enum, auto


class EnabledColors(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    BLACK = auto()


v = EnabledColors.RED
# v sera EnabledColors.RED
c = EnabledColors.RED

if c == v:
    ...
print(c.value)
