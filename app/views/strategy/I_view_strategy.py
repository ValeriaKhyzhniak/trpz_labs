from abc import ABC, abstractmethod


class IViewStrategy(ABC):
    @abstractmethod
    def create_operating_window(self, window):
        pass
