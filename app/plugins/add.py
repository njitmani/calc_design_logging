from app.commands import Command
import logging

class AddCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            result = sum(numbers)
            logging.info(f"Result: {result}")
        except ValueError:
            logging.error("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return AddCommand()

