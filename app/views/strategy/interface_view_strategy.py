from abc import ABC, abstractmethod


class InterfaceViewStrategy(ABC):
    @abstractmethod
    def create_operating_window(self, window):
        pass
