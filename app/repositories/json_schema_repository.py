from I_json_schema_repository import IJSONSchemaRepository
from repository import Repository
from app.models.json_schema import JSONSchema


class JSONSchemaRepository(IJSONSchemaRepository, Repository):
    def __init__(self, json_schema: JSONSchema):
        super().__init__()
        self.json_schema = json_schema

    def get_by_name(self):
        pass
