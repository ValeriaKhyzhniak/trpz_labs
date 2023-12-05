from abc import *
from app.repositories.I_repository import IRepository


class IHistoryRepository(IRepository):

    @abstractmethod
    def delete_all(self):
        pass

