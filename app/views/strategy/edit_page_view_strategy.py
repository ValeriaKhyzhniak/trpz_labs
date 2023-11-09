import tkinter as tk
from tkinter import *
import ctypes
from tkinter import ttk

from app.views.strategy.I_view_strategy import IViewStrategy


class EditPageViewStrategy(IViewStrategy):
    font = ('Consolas 20', 18)
    # Створюємо змінну для збереження шляху відкритого файлу
    _opened_file = ''
    # Створюємо змінну для збереження вікна з текстом
    _schema_text = Text

    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()

    def create_operating_window(self, edit_page):
        # Створюємо об'єкт рамки
        self.schema_frame = LabelFrame(edit_page, width=100, height=70, text='JSONSchema', padx=25, pady=20,
                                       font=self.font)
        # Створюємо об'єкт текстового поля для редагування JSON-схеми
        self.schema_text = Text(self.schema_frame, font=self.font, width=40, height=20, wrap=tk.NONE)
        # Розташовуємо текстове поле у рамці
        self.schema_text.pack(fill=BOTH, expand=True)
        # Розташовуємо рамку у лівій частині вікна
        self.schema_frame.pack(side=LEFT, fill=BOTH, expand=True)
        edit_page.add(self.schema_frame, text='name')
        # Розташуємо вкладку вгорі сторінки
        edit_page.place(relx=0, rely=0, anchor='nw')
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
