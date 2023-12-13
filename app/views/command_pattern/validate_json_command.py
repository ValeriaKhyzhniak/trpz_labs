from app.services.json_schema_service import JSONSchemaService
from app.views.command_pattern.interface_command import InterfaceCommand


class ValidateJSONCommand(InterfaceCommand):
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self, schema_text):
        super().__init__()
        self.schema_text = schema_text

    def execute(self):
        # Викликаємо метод валідації json
        return self.json_schema_service.validate_schema(self.schema_text)
