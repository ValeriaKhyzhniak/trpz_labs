from abc import *
from I_repository import IRepository


class IHistoryRepository(IRepository):

    @abstractmethod
    def delete_all(self):
        pass

