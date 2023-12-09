from app.services.json_schema_service import JSONSchemaService
from app.views.command_puttern.interface_command import InterfaceCommand


class ExportJSONCommand(InterfaceCommand):
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self):
        super().__init__()

    def execute(self):
        # Викликаємо метод експорту json як таблиці Markdown
        self.json_schema_service.export_schema()
        print("Export completed!")
