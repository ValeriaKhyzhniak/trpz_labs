import tkinter as tk
from tkinter import ttk
from tkinter import *
from application.client.gui.view_elements.pages.interface_view_strategy import InterfaceViewStrategy
from application.client.gui.view_elements.toolbar_view import ToolbarView


class EditPageViewStrategy(InterfaceViewStrategy):
    font = ('Consolas 20', 18)
    # # Створюємо змінну для збереження шляху відкритого файлу
    # _opened_file = ''
    # # Створюємо змінну для збереження вікна з текстом
    # _schema_text = Text
    toolbar_view = ToolbarView()

    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()

    def create_application_tab_frame(self, application_tab, path):
        self.main_frame = ttk.Frame(application_tab)
        # Створюємо об'єкт рамки
        self.json_schema_frame = LabelFrame(self.main_frame, text='JSONSchema', padx=25, pady=20,
                                            font=self.font)
        (self.json_schema_frame.grid(column=1, row=0))
        # Створюємо об'єкт текстового поля для редагування JSON-схеми
        self.json_schema_text = Text(self.json_schema_frame, width=35, height=15, font=self.font, wrap=tk.NONE)
        # Розташовуємо текстове поле у рамці
        self.json_schema_text.pack(fill=BOTH, expand=True)
        self.toolbar = self.toolbar_view.create_toolbar(self.main_frame, self.json_schema_text)
        # Розташовуємо панель інструментів
        self.toolbar.grid(row=0, column=0)
        self.main_frame.pack()
        # Create a Style to configure the tabs
        self.style = ttk.Style()
        self.style.configure("TNotebook.Tab", padding=[1, 1])  # You can adjust padding as needed

        application_tab.add(self.main_frame, text=path)
        return self.json_schema_text

    # @property
    # def opened_file(self):
    #     return self._opened_file
    #
    # @opened_file.setter
    # def opened_file(self, value):
    #     self._opened_file = value
    #
    # @property
    # def json_schema_text(self):
    #     return self._schema_text
    #
    # @json_schema_text.setter
    # def json_schema_text(self, value):
    #     self._schema_text = value
