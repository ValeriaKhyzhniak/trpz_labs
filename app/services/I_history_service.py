from abc import ABC, abstractmethod


class IHistoryService(ABC):

    @abstractmethod
    def open_history(self):
        pass

    @abstractmethod
    def delete_history(self):
        pass
