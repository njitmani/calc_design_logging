from app.commands import Command
import logging

class DivideCommand(Command):
    def execute(self, *args):
        try:
            numbers = [float(arg) for arg in args]
            if len(numbers) < 2:
                logging.error("Error: Need at least two numbers to perform division.")
                return
            result = numbers.pop(0)
            for denominator in numbers:
                if denominator == 0:
                    logging.error("Error: Division by zero is not allowed.")
                    return
                result /= denominator
            logging.info(f"Result: {result}")
        except ValueError:
            logging.error("Error: All arguments must be numbers.")

def get_command_instance(command_handler=None):
    return DivideCommand()
