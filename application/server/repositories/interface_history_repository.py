from abc import *
from application.server.repositories.interface_repository import InterfaceRepository


class InterfaceHistoryRepository(InterfaceRepository):

    @abstractmethod
    def delete_all(self):
        pass

