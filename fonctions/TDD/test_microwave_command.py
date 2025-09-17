import pytest

from fonctions.TDD.microwave_command import manage_microwave_command


def test_microwave_command_handle_open():

    command_result = manage_microwave_command(command="Open")

    assert command_result == "The door has been opened."

def test_microwave_command_handle_close():
    command_result = manage_microwave_command(command="Close")

    assert command_result == "The door has been closed."

def test_microwave_command_handle_launch():
    command_result = manage_microwave_command(command="Launch")

    assert command_result == "The door has been launched."


def test_microwave_generate_error_with_invalid_command():
    with pytest.raises(ValueError):
        manage_microwave_command(command="chaudron")
