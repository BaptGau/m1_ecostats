# from typing import Tuple
#
#
# def function() -> Tuple[str, int]:
#     return "one", 1
#
# result = function()
# print(type(result))
from typing import Tuple

t = ("one", 1)
print(t[0], t[1])
# t[0] = "bonjour"

# Exercice
# Créer une fonction qui prend un entier (param) en paramètre
# et renvoie param**2, param**4, param**6
# Créer un nouveau nombre n qui est la somme de ces éléments
# puis print -> param**6, param**4, param**2, n

def powers(param: int) -> Tuple[int, int, int]:
    return param**2, param**4, param**6

if __name__ == "__main__":
    param = 4
    pow_2, pow_4, pow_6 = powers(param)
    sum_powers = pow_2 + pow_4 + pow_6
    print(pow_6, pow_4, pow_2, sum_powers)





