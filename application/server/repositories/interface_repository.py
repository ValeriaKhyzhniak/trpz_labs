from abc import ABC, abstractmethod


class InterfaceRepository(ABC):

    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def delete_by_id(self, entity_id):
        pass

    @abstractmethod
    def _insert(self, entity):
        pass

    @abstractmethod
    def _update(self, entity):
        pass
