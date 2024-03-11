from app.commands import Command
import logging

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                logging.error("Error: Need at least two numbers to perform subtraction.")
                return
            result = numbers.pop(0) - sum(numbers)
            logging.info(f"Result: {result}")
        except ValueError:
            logging.error("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return SubtractCommand()
