from enum import Enum
from typing import Literal


class EnabledColors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    BLACK = "black"


color = EnabledColors.GREEN


def func(color: Literal["red", "green", "blue", "yellow", "black"]):
    match color:
        case "red":
            ...  # fé des trucs avec la couleur


def func_enum(color: EnabledColors) -> None:
    match color:
        case EnabledColors.RED:
            print("C'est rouge")
        case EnabledColors.GREEN:
            print("C'est vert")
        case EnabledColors.BLUE:
            print("C'est bleu")
        case EnabledColors.YELLOW:
            print("C'est jaune")
        case EnabledColors.BLACK:
            print("C'est noir")


v = EnabledColors("red")
# v sera EnabledColors.RED
c = EnabledColors.GREEN
print(c.value)
