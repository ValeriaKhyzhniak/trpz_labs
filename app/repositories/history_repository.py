from I_history_repository import IHistoryRepository
from repository import Repository
from app.models.json_history import JSONHistory


class HistoryRepository(IHistoryRepository, Repository, JSONHistory):
    def __init__(self, json_history: JSONHistory):
        super().__init__()
        self.json_history = json_history

    def delete_all(self):
        pass
