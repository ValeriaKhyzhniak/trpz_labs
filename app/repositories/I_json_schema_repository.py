from abc import *
from I_repository import IRepository


class IJSONSchemaRepository(IRepository):

    @abstractmethod
    def get_by_name(self):
        pass
