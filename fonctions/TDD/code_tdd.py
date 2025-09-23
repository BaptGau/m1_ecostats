from typing import Literal


def calculatrice(x: int | float, y: int | float, instruction: Literal["add", "subtract", "multiply", "divide"]) -> float:
    is_x_numeric = isinstance(x, (int, float))
    is_y_numeric = isinstance(y, (int, float))
    if not is_x_numeric or not is_y_numeric:
        raise TypeError(f"Both types should be int or float.")
    match instruction:
        case "add":
            return x+y
        case "subtract":
            return x-y
        case "divide":
            return x/y
        case "multiply":
            return x*y
        case _:
            raise NotImplementedError(f"Instruction {instruction} not implemented.")