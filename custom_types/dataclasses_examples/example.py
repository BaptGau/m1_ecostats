# refaire la calculette pour la 17 e fois
# avec une opération qui est toujours un enum
# La sortie doit contenir trois éléments:
# - Le résultat du calcul
# - Opération réalisée
# - Le vecteur des entrées (x, y)


from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple


class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

@dataclass
class ComputationResult:
    result: int | float
    operation: Operation
    input_variables: Tuple[int | float, int | float]

def calculatrice(x: int, y: int, operation: Operation) -> ComputationResult:
    match operation:
        case Operation.ADD:
            c1 = ComputationResult(
                result=x + y,
                operation=operation,
                input_variables=(x, y),
            )
        case Operation.SUBTRACT:
            ...
        case _:
            raise ValueError(f"Unknown operation {operation}")