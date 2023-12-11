from tkinter import *
from app.services.json_schema_service import JSONSchemaService
from app.views.create_new_page import CreateNewPage
from app.views.strategy.edit_page_view_strategy import EditPageViewStrategy


class MenuView:
    # Створюємо об'єкт класу CreateNewPage()
    create_new_window = CreateNewPage()
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()

    def __init__(self):
        super().__init__()

    # Створюємо меню для вікна
    def create_menu(self, window):
        # Створюємо об'єкт меню
        self.menu = Menu()
        # Додаємо пункт меню "Файл"
        self.file_menu = Menu(self.menu, tearoff=0, font=("Helvetica", 16))
        self.menu.add_cascade(label="Файл", menu=self.file_menu, font=("Helvetica", 16))
        self.file_menu.add_command(label="Відкрити", font=('Helvetica', 20)
                                   , command=lambda: self.create_new_window.open_new_window(window))
        self.file_menu.add_command(label="Зберегти", font='10'
                                   , command=lambda: self.json_schema_service.
                                   save_file(EditPageViewStrategy.schema_text, EditPageViewStrategy.opened_file))
        self.file_menu.add_command(label="Зберегти як...", font='10'
                                   # , command_puttern=lambda: self.json_schema_service.save_as_file()
                                    )
        # self.protocol("WM_DELETE_WINDOW", self.on_closing)
        return self.menu
