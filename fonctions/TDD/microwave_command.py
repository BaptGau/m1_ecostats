# Open
# Close
# Launch
from typing import Literal


def manage_microwave_command(command: Literal["Open", "Close", "Launch"]) -> str:
    match command:
        case "Open":
            return "The door has been opened."
        case "Close":
            return "The door has been closed."
        case "Launch":
            return "The door has been launched."
        case _:
            raise ValueError(f"Invalid command: '{command}")
