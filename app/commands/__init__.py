from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class ExitApplication(Exception):
    """Exception raised to signal application exit."""
    pass
