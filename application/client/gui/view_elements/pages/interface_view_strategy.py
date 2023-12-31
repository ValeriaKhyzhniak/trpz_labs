from abc import ABC, abstractmethod


class InterfaceViewStrategy(ABC):
    @abstractmethod
    def create_application_tab_frame(self, window, name):
        pass
