from tkinter import ttk
import tkinter as tk
from tkinter import *
import ctypes
from app.views.view_elements.menu_view import MenuView
from app.views.I_json_schema_view import IJSONSchemaView
from app.views.strategy.first_page_view_strategy import FirstPageViewStrategy
from app.views.strategy.view_context import ViewContext


# Створюємо клас для нашого додатку
class JSONSchemaView(Tk, IJSONSchemaView):
    menu_view = MenuView()
    # Змінна для збереження стилю шрифту
    font = ('Consolas 20', 18)

    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()
        # Встановлюємо назву вікна
        self.title("JSON Schema Editor")
        # Встановлюємо розмір вікна
        self.geometry("1200x600")
        # Встановлюємо DPI-свідомість процесу в Windows, для того щоб програма могла змінювати
        # масштаб елементів інтерфейсу користувача, щоб вони виглядали на екрані більш чітко
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        # Створюємо об'єкт класу Style(), щоб налаштувати власний стиль
        s = ttk.Style()
        # Змінюємо розмір шрифту
        s.configure('TNotebook.Tab', font=self.font)
        # Створюємо контейнер, щоб можна було відображати декілька вкладок
        self.window = ttk.Notebook()
        # Розміщуємо об'єкт на головному вікні
        self.window.pack(expand=True)
        # Додаємо меню
        self.config(menu=self.menu_view.create_menu(self.window))
        # Створюємо початкову сторінку
        self.welcome_page = ViewContext(FirstPageViewStrategy()).view_page_strategy(self.window)
