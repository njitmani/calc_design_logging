from app.commands import Command, ExitApplication
import logging

class ExitCommand(Command):
    def execute(self, *args):
        logging.info("Exiting...")
        raise ExitApplication

def get_command_instance(command_handler=None):
    return ExitCommand()
