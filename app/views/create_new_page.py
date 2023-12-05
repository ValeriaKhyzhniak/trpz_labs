from app.services.json_schema_service import JSONSchemaService
from app.views.strategy.edit_page_view_strategy import EditPageViewStrategy
from app.views.strategy.view_context import ViewContext


class CreateNewPage:
    json_schema_service = JSONSchemaService()

    def __init__(self):
        super().__init__()

    def open_new_window(self, window):
        # Створюмо сторінку для редагування
        schema_text = ViewContext(EditPageViewStrategy()).view_page_strategy(window)
        # Відкриваємо в неї вміст файлу
        op_file = self.json_schema_service.open_file(schema_text)
        # Записуємо значення в сеттери
        EditPageViewStrategy.opened_file = op_file
        EditPageViewStrategy.schema_text = schema_text

    def create_new_window(self):
        pass
