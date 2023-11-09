from I_history_service import IHistoryService
from app.repositories.I_history_repository import IHistoryRepository


class JSONHistoryService(IHistoryService):

    def __init__(self, history_repository: IHistoryRepository):
        super().__init__()
        self.history_repository = history_repository

    def open_history(self):
        pass

    def delete_history(self):
        pass
