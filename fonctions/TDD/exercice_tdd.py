# Recoder la calculatrice en TDD (avec des tests en tout cas)
# Exercice
# Faire une fonction "calculatrice" qui prend en paramètres 3 éléments:
# 2 nombres décimaux et une instruction ["add", "subtract", "multiply", "divide"]
# la fonction return l'opération correspondante.
# bonus: bien typé
from typing import Literal

import pytest

from fonctions.TDD.code_tdd import calculatrice


def test_calculatrice_handle_addition_with_two_integers():
    x = 3
    y = 4

    assert calculatrice(x=x, y=y, instruction="add") == x + y


def test_calculatrice_handle_addition_with_two_floats():
    x = 3.0
    y = 14.0

    assert calculatrice(x=x, y=y, instruction="add") == x + y


def test_operation_raise_error_if_type_is_not_numeric():
    x = "foo"
    y = "bar"

    with pytest.raises(TypeError):
        assert calculatrice(x=x, y=y, instruction="add")



def test_substract_between_two_integers():
    x = 10
    y = 5

    assert calculatrice(x=x, y=y, instruction="subtract") == x - y

...

def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        calculatrice(x=100, y=0, instruction="divide")

...

def test_calculatrice_handle_multiplication_with_two_integers():
    x = 10
    y = 5

    assert calculatrice(x=x, y=y, instruction="multiply") == x * y