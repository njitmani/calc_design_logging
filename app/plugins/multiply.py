from app.commands import Command
import logging

class MultiplyCommand(Command):
    def execute(self, *args):
        try:
            result = 1
            for arg in args:
                result *= float(arg)
            logging.info(f"Result: {result}")
        except ValueError:
            logging.error("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return MultiplyCommand()
