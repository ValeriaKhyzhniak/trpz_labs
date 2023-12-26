from tkinter import ttk
from tkinter import *
import ctypes
from app.views.flyweight_pattern.text_style_flyweight_factory import TextStyleFlyweightFactory
from app.views.view_elements.menu_view import MenuView
from app.views.I_json_schema_view import IJSONSchemaView
from app.views.strategy.first_page_view_strategy import FirstPageViewStrategy
from app.views.strategy.view_context import ViewContext


# Створюємо клас для нашого додатку
class JSONSchemaView(Tk, IJSONSchemaView):
    menu_view = MenuView()
    # Створюємо фабрику
    text_style_factory = TextStyleFlyweightFactory()
    # Створюємо загальний стиль для тексту
    _common_style = text_style_factory.get_style("Consolas", 20, "black")

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
        # Змінюємо стиль тексту (в параметр font передаємо значення з загального стилю)
        s.configure('TNotebook.Tab', font=(self._common_style.font_family, self._common_style.font_size))
        # Створюємо контейнер, щоб можна було відображати декілька вкладок
        self.window = ttk.Notebook()
        # Розміщуємо об'єкт на головному вікні
        self.window.pack(expand=True)
        # Додаємо меню
        self.config(menu=self.menu_view.create_menu(self.window))
        # Створюємо початкову сторінку
        self.welcome_page = ViewContext(FirstPageViewStrategy()).view_page_strategy(self.window)

    @property
    def common_style(self):
        return self._common_style

    @common_style.setter
    def common_style(self, value):
        self._common_style = value
