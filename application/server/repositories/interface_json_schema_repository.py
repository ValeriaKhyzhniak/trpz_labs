from abc import *
from application.server.repositories.interface_repository import InterfaceRepository


class InterfaceJSONSchemaRepository(InterfaceRepository):

    @abstractmethod
    def get_by_name(self, name):
        pass

    @abstractmethod
    def get_last_element(self):
        pass
