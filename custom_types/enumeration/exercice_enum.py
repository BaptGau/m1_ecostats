# Exercice enum:
# Recoder la fonction calculatrice avec une instruction qui est un enum
from enum import Enum, auto

class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()


def calculatrice(x: int, y: int, operation: Operation) -> int | float:
    match operation:
        case Operation.ADD:
            return x + y
        case Operation.SUBTRACT:
            return x - y
        case Operation.MULTIPLY:
            return x * y
        case Operation.DIVIDE:
            return x / y
        case _:
            raise ValueError(f"Unknown operation {operation}")