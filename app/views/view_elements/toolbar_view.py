from tkinter import *
from app.services.json_schema_service import JSONSchemaService
from app.views.command_pattern.export_json_command import ExportJSONCommand
from app.views.command_pattern.flatten_schema_command import FlattenSchemaCommand
from app.views.command_pattern.validate_json_command import ValidateJSONCommand
from app.views.observer_pattern.export_button_observer import ExportButtonObserver
from app.views.observer_pattern.flatten_view_button_observer import FlattenViewButtonObserver
from app.views.observer_pattern.validate_button_observer import ValidateButtonObserver
from app.views.observer_pattern.button_subject import ButtonSubject


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
        self.validate_button = ButtonSubject(self.toolbar, "Валідувати", validate_json_command)
        # Створюємо спостерігача
        validate_observer = ValidateButtonObserver()
        # Додаємо спостерігача для
        self.validate_button.add_observer(validate_observer)
        # Створюємо команду експорту validate_button
        export_json_command = ExportJSONCommand()
        # Додаємо кнопку для експорту JSON-схеми як таблиці Markdown
        self.export_button = ButtonSubject(self.toolbar, "Експортувати", export_json_command)
        # Створюємо спостерігача
        export_observer = ExportButtonObserver()
        # Додаємо спостерігача для
        self.export_button.add_observer(export_observer)
        # Створюємо команду перетворення JSON-схеми в "flatten" вигляд
        flatten_schema_command = FlattenSchemaCommand(schema_text)
        # Додаємо кнопку для перетворення JSON-схеми в "flatten" вигляд
        self.flatten_button = ButtonSubject(self.toolbar, "Flatten view", flatten_schema_command)
        # Створюємо спостерігача
        flatten_observer = FlattenViewButtonObserver()
        # Додаємо спостерігача для
        self.flatten_button.add_observer(flatten_observer)
        return self.toolbar

