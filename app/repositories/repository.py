from I_repository import IRepository
from app.models.json_history import JSONHistory
from app.models.json_schema import JSONSchema


class Repository(IRepository):
    def __init__(self, json_schema: JSONSchema, json_history: JSONHistory):
        super().__init__()
        self.json_schema = json_schema
        self.json_history = json_history

    def get_by_id(self):
        pass

    def delete_by_id(self):
        pass

    def insert(self):
        pass
