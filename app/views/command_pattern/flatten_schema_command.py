from app.services.json_schema_service import JSONSchemaService
from app.views.command_pattern.interface_command import InterfaceCommand


class FlattenSchemaCommand(InterfaceCommand):
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self, schema_text):
        super().__init__()
        self.schema_text = schema_text

    def execute(self):
        # Викликаємо метод для перетворення json в flatten вигляд
        return self.json_schema_service.flatten_schema(self.schema_text)
