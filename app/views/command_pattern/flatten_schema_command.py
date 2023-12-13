from app.services.json_schema_service import JSONSchemaService
from app.views.command_pattern.interface_command import InterfaceCommand


class FlattenSchemaCommand(InterfaceCommand):
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self):
        super().__init__()

    def execute(self):
        # Викликаємо метод для перетворення json в flatten вигляд
        self.json_schema_service.flatten_schema()
        print("JSON to flatten view completed!")
