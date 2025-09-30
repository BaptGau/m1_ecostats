# refaire la calculette pour la 17 e fois
# avec une opération qui est toujours un enum
# La sortie doit contenir trois éléments:
# - le résultat du calcul
# - le temps d'exécution
# - Opération réalisée
# - (bonus): Le vecteur des entrées (x, y)


from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple, Callable, Any
from time import time


class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

@dataclass
class ComputationResult:
    result: int | float
    execution_time: float
    operation: Operation
    input_variables: Tuple[int | float, int | float]

def track_time(func: Callable) -> Tuple[Any, float]:
    start = time()
    result = func()
    end = time()
    return result, end - start

def calculatrice(x: int, y: int, operation: Operation) -> ComputationResult:
    match operation:
        case Operation.ADD:

            start_time = time()
            add_result = x + y
            end_time = time()

            exec_time = end_time - start_time

            return ComputationResult(
                result=add_result,
                operation=operation,
                input_variables=(x, y),
                execution_time=exec_time,
            )
        case Operation.SUBTRACT:
            sub_result, exec_time = track_time(func=lambda x, y: x - y)

            return ComputationResult(
                result=sub_result,
                operation=operation,
                input_variables=(x, y),
                execution_time=exec_time,
            )       
        case _:
            raise ValueError(f"Unknown operation {operation}")