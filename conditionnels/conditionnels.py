from typing import Literal

variable = 10

if variable > 0:
    print("La variable est positive")
else:
    print("La variable n'est pas positive")

if variable < 0:
    print("La variable est négative")
elif variable == 0:
    print("La variable est nulle")
else:
    print("La variable est positive ou nulle")

if variable != 0:
    print("La variable est différente de zéro")
else:
    print("La variable est égale à zéro")


couleurs: Literal["rouge", "vert", "bleu", "jaune", "noir"] = "chaudron"


if couleurs == "rouge":
    if variable == 0:
        ...
elif couleurs == "vert":
    ...
elif couleurs == "bleu":
    print(...)


match couleurs:
    case "rouge":
        print("0000FF")
    case "vert":
        print("00FF00")
    case "bleu":
        print("FF0000")
    case "jaune":
        print("FFFF00")
    case "noir":
        print("000000")
    case _:
        print("Couleur inconnue")
        raise ValueError("Couleur inconnue")

var = "bonjour"
