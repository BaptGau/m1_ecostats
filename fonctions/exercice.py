# Exercice
# Faire une fonction "calculatrice" qui prend en paramètres 3 éléments:
# 2 nombres décimaux et une instruction ["add", "subtract", "multiply", "divide"]
# la fonction return l'opération correspondante.
# bonus: bien typé
from typing import Literal


def calculatrice(x: int | float, y : int | float, instruction: Literal["add", "subtract", "multiply", "divide", "approximate_divide"]) -> int | float:
    match instruction:
        case "add":
            return x + y
        case "subtract":
            return x - y
        case "multiply":
            return x * y
        case "divide":
            if y == 0:
                raise ZeroDivisionError(f"Got x: {x}, y: {y}")
            return x / y
        case "approximate_divide":
            return x / (y+10e-6)
        case _:
            raise ValueError(f"Invalid instruction: {instruction} - Expected 'add', 'subtract', 'multiply', 'divide', or 'approximate_divide'")




result = calculatrice(10, 0, "divide")






