from typing import Literal


def manage_micro_wave_commands(command_to_run: Literal["Open", "Close", "Launch"]) -> str:
    """
    Manage the micro-wave commands and execute things accordingly.
    the command should be "Open", "Close" or "Launch".
    """
    match command_to_run:
        case "Open":
            # envoyer un signal ailleurs
            return "Micro-ondes ouvert"
        case "Close":
            return "Couleur ouvert"
        case "Launch":
            return "Lancement de la cuisson"
        case _:
            raise ValueError("Commande non connue")

v = manage_micro_wave_commands("Open")
status = f"Micro-wave status: {v}"
print(status)


def add(x: int, y: int) -> int:
    return x + y


result = add(x=1, y=2)
result2 = add(x=result, y=5)
result3 = add(x=result2, y=6)










