from .command_handler import CommandHandler
from .commands import ExitApplication
import os
import importlib.util
import logging

class App:
    command_handler = CommandHandler()

    @classmethod
    def configure_logging(cls):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @classmethod
    def load_plugins(cls, directory="plugins"):
        cls.configure_logging()
        base_dir = os.path.dirname(__file__)
        plugins_dir = os.path.abspath(os.path.join(base_dir, directory))
        logging.info("Loading plugins...")

        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                module_path = os.path.join(plugins_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                command_instance = module.get_command_instance(cls.command_handler)
                cls.command_handler.register_command(module_name, command_instance)
                logging.info(f"Loaded plugin: {module_name}")

    @classmethod
    def start(cls):
        cls.load_plugins()
        logging.info("Hello World. Type 'exit' to exit.")
        try:
            while True:
                input_text = input("").strip()
                if not input_text:
                    continue
                parts = input_text.split(' ')
                command_name = parts[0]
                args = parts[1:]

                if command_name in cls.command_handler.commands:
                    cls.command_handler.execute_command(command_name, *args)
                else:
                    logging.info("Unknown command. Type 'exit' to exit.")

        except ExitApplication:
            logging.info("Exiting...")
