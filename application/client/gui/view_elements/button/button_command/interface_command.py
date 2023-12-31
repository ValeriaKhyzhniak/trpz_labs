from abc import ABC, abstractmethod


class InterfaceCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
