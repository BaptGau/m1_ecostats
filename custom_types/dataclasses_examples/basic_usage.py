from dataclasses import dataclass
from enum import Enum, auto
from typing import Literal


class AppreciationPython(Enum):
    NUL = auto()
    MOYEN = auto()
    SUPER = auto()
    EN_MAITRISE = auto()


@dataclass
class ParametresOrdinateur:
    os: Literal["MacOs", "Linux", "Windows"]
    python_version: str


@dataclass
class Etudiant:
    name: str
    age: int
    niveau_appreciation_cours_python: AppreciationPython
    parametres: ParametresOrdinateur


moi = Etudiant(
    name="Baptiste",
    age=25,
    niveau_appreciation_cours_python=AppreciationPython.EN_MAITRISE,
    parametres=ParametresOrdinateur(
        os="MacOs",
        python_version="3.12.0",
    ),
)

print(moi)
