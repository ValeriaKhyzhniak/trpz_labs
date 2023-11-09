from abc import *
from app.repositories.I_repository import IRepository


class IJSONSchemaRepository(IRepository):

    @abstractmethod
    def get_by_name(self, name):
        pass
