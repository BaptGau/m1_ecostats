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


# custom_types/dataclasses_examples/example.py


def calculatrice(x: int, y: int, operation: Operation) -> ComputationResult:
    computation_result = None

    match operation:
        case Operation.ADD:
            computation_result = x + y

        case Operation.SUBTRACT:
            computation_result = x - y

        case Operation.MULTIPLY:
            computation_result = x * y

        case Operation.DIVIDE:
            computation_result = x / y
        case _:
            raise ValueError(f"Unknown operation {operation}")

    return ComputationResult(
        result=computation_result,
        operation=operation,
        input_variables=(x, y),
    )


result_object = calculatrice(x=1, y=2, operation=Operation.ADD)
print(result_object)
