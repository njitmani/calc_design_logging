"""Unit tests for the calculator app."""
import pytest
import logging
from io import StringIO
from app import App
from unittest.mock import patch

@pytest.fixture
def app():
    return App()

@pytest.mark.skip(reason="temporarily skipping while fixing")
def test_application_flow(caplog, app):
    with patch('builtins.input', side_effect=['add 1 2', 'subtract 1 3', 'exit']):
        app.start()

    expected_logs = [
            "INFO     root:__init__.py:19 Loading plugins...",
            "INFO     root:command_handler.py:9 Command 'divide' registered.",
            "INFO     root:__init__.py:30 Loaded plugin: divide",
            "INFO     root:command_handler.py:9 Command 'multiply' registered.",
            "INFO     root:__init__.py:30 Loaded plugin: multiply",
            "INFO     root:command_handler.py:9 Command 'subtract' registered.",
            "INFO     root:__init__.py:30 Loaded plugin: subtract",
            "INFO     root:command_handler.py:9 Command 'exit' registered.",
            "INFO     root:__init__.py:30 Loaded plugin: exit",
            "INFO     root:command_handler.py:9 Command 'menu' registered.",
            "INFO     root:__init__.py:30 Loaded plugin: menu",
            "INFO     root:command_handler.py:9 Command 'add' registered.",
            "INFO     root:__init__.py:30 Loaded plugin: add",
            "INFO     root:__init__.py:35 Hello World. Type 'exit' to exit.",
            "INFO     root:add.py:9 Result: 3.0",
            "INFO     root:subtract.py:12 Result: -2.0",
            "INFO     root:exit.py:6 Exiting...",
            "INFO     root:__init__.py:51 Exiting..."
    ]

    # Adjust the log message check to ignore specific formatting and focus on content
    for expected_log in expected_logs:
        assert any(expected_log in message for message in caplog.text), f"Log not found: {expected_log}"

def test_app_start_exit_command(capfd, monkeypatch,log_output):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    #out, _ = capfd.readouterr()
    log_contents = log_output.getvalue()
    # Check that the initial greeting is printed and the REPL exits gracefully
    #print(log_contents)
    assert "Hello World. Type 'exit' to exit." in log_contents
    assert "Exiting..." in log_contents

def test_app_start_unknown_command(capfd, monkeypatch, log_output):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    #print(log_contents)
    assert "Hello World. Type 'exit' to exit." in log_contents
    assert "Unknown command. Type 'exit' to exit." in log_contents
    assert "Exiting..." in log_contents

def test_add_command(capfd, monkeypatch, log_output):
    """Test adding numbers using the 'add' command."""
    inputs = iter(['add 2 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Result: 7" in log_contents

def test_subtract_command(capfd, monkeypatch, log_output):
    """Test subtracting numbers using the 'subtract' command."""
    inputs = iter(['subtract 10 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Result: 7" in log_contents

def test_multiply_command(capfd, monkeypatch, log_output):
    """Test multiplying numbers using the 'multiply' command."""
    inputs = iter(['multiply 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Result: 6" in log_contents

def test_divide_command(capfd, monkeypatch, log_output):
    """Test dividing numbers using the 'divide' command."""
    inputs = iter(['divide 6 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Result: 3" in log_contents

def test_menu_command(capfd, monkeypatch, log_output):
    """Test displaying the menu using the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Available commands:" in log_contents

def test_divide_by_zero(capfd, monkeypatch, log_output):
    """Test divide by zero error handling."""
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Error: Division by zero is not allowed." in log_contents

def test_invalid_number(capfd, monkeypatch, log_output):
    """Test error handling for non-numeric input."""
    inputs = iter(['add 10 two', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Error: All arguments must be numbers." in log_contents

def test_exit_command(capfd, monkeypatch, log_output):
    """Test the exit command triggers application exit."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Exiting..." in log_contents

def test_unrecognized_command(capfd, monkeypatch, log_output):
    """Test handling of an unrecognized command."""
    inputs = iter(['fake_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Unknown command. Type 'exit' to exit." in log_contents
    assert "Hello World. Type 'exit' to exit." in log_contents

def test_divide_by_zero_command(capfd, monkeypatch, log_output):
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Error: Division by zero is not allowed." in log_contents

def test_multiply_with_invalid_number(capfd, monkeypatch, log_output):
    inputs = iter(['multiply 10 two', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Error: All arguments must be numbers." in log_contents

def test_subtract_less_than_two_numbers(capfd, monkeypatch, log_output):
    inputs = iter(['subtract 10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    log_contents = log_output.getvalue()
    assert "Error: Need at least two numbers to perform subtraction." in log_contents

def test_add_command_with_invalid_arguments(capfd, monkeypatch, log_output):
    """
    Test add command execution with invalid arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['add 10 two', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    log_contents = log_output.getvalue()
    assert "Error: All arguments must be numbers." in log_contents

def test_subtract_command_with_invalid_arguments(capfd, monkeypatch, log_output):
    """
    Test subtract command execution with invalid arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['subtract 10 two', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    log_contents = log_output.getvalue()
    assert "Error: All arguments must be numbers." in log_contents

def test_divide_command_with_invalid_arguments(capfd, monkeypatch, log_output):
    """
    Test divide command execution with invalid arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['divide 10 two', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    log_contents = log_output.getvalue()
    assert "Error: All arguments must be numbers." in log_contents

def test_divide_command_with_insufficient_arguments(capfd, monkeypatch, log_output):
    """
    Test divide command execution with insufficient arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['divide 10', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    log_contents = log_output.getvalue()
    assert "Error: Need at least two numbers to perform division." in log_contents
