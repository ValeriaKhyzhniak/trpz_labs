from tkinter import *
from app.services.json_schema_service import JSONSchemaService
from app.views.command_puttern.button_involker import ButtonInvoker
from app.views.command_puttern.export_json_command import ExportJSONCommand
from app.views.command_puttern.flatten_schema_command import FlattenSchemaCommand
from app.views.command_puttern.validate_json_command import ValidateJSONCommand


class ToolbarView:
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self):
        super().__init__()

    # Створюємо панелі інструментів
    def create_toolbar(self, main_frame, schema_text):
        # Створюємо об'єкт панелі інструментів
        self.toolbar = Frame(main_frame)
        # Створюємо команду валідації
        validate_json_command = ValidateJSONCommand(schema_text)
        # Додаємо кнопку для валідації JSON-схеми
        self.validate_button = Button(self.toolbar, text="Валідувати", command=ButtonInvoker(validate_json_command).invoke)
        self.validate_button.grid(row=0, column=0, pady=20, padx=0)
        # Створюємо команду експорту
        export_json_command = ExportJSONCommand()
        # Додаємо кнопку для експорту JSON-схеми як таблиці Markdown
        self.export_button = Button(self.toolbar, text="Експортувати", command=ButtonInvoker(export_json_command).invoke)
        self.export_button.grid(row=1, column=0, pady=20, padx=0)
        # Створюємо команду перетворення JSON-схеми в "flatten" вигляд
        flatten_schema_command = FlattenSchemaCommand()
        # Додаємо кнопку для перетворення JSON-схеми в "flatten" вигляд
        self.flatten_button = Button(self.toolbar, text="Flatten view", command=ButtonInvoker(flatten_schema_command).invoke)
        self.flatten_button.grid(row=2, column=0, pady=20, padx=0)
        return self.toolbar

