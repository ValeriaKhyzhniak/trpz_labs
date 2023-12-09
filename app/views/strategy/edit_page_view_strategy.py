import tkinter as tk
from tkinter import *
from app.views.strategy.interface_view_strategy import InterfaceViewStrategy
from app.views.view_elements.toolbar_view import ToolbarView


class EditPageViewStrategy(InterfaceViewStrategy):
    font = ('Consolas 20', 18)
    # Створюємо змінну для збереження шляху відкритого файлу
    _opened_file = ''
    # Створюємо змінну для збереження вікна з текстом
    _schema_text = Text
    toolbar_view = ToolbarView()

    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()

    def create_operating_window(self, edit_page):
        self.main_frame = Frame(edit_page, padx=25, pady=20)

        # Створюємо об'єкт рамки
        self.schema_frame = LabelFrame(self.main_frame, text='JSONSchema', padx=25, pady=20,
                                       font=self.font)
        (self.schema_frame.grid(column=1, row=0))
        # Створюємо об'єкт текстового поля для редагування JSON-схеми
        self.schema_text = Text(self.schema_frame, width=35, height=15, font=self.font, wrap=tk.NONE)
        # Розташовуємо текстове поле у рамці
        self.schema_text.pack(fill=BOTH, expand=True)
        self.toolbar = self.toolbar_view.create_toolbar(self.main_frame, self.schema_text)
        # Розташовуємо панель інструментів
        self.toolbar.grid(row=0, column=0)
        self.main_frame.pack()
        edit_page.add(self.main_frame, text='name')
        return self.schema_text

    @property
    def opened_file(self):
        return self._opened_file

    @opened_file.setter
    def opened_file(self, value):
        self._opened_file = value

    @property
    def schema_text(self):
        return self._schema_text

    @schema_text.setter
    def schema_text(self, value):
        self._schema_text = value
