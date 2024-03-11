import logging

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command):
        self.commands[command_name] = command
        logging.info(f"Command '{command_name}' registered.")

    def execute_command(self, command_name: str, *args):
        if command_name in self.commands:
            self.commands[command_name].execute(*args)
        else:
            logging.error(f"No such command: '{command_name}'")
