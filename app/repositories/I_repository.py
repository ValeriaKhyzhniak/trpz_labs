from abc import ABC, abstractmethod


class IRepository(ABC):

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def delete_by_id(self):
        pass

    @abstractmethod
    def insert(self):
        pass
