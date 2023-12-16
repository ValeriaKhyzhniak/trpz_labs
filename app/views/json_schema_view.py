import tkinter as tk
from app.services.json_schema_service import JSONSchemaService
from app.views.I_json_schema_view import IJSONSchemaView
from tkinter import *
import ctypes


# Створюємо клас для нашого додатку
class JSONSchemaView(Tk, IJSONSchemaView):
    # Створюємо об'єкт класу JSONSchemaService()
    json_schema_service = JSONSchemaService()
    # Створюємо змінну для збереження шляху відкритого файлу
    opened_file = ''

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
        # Створюємо об'єкт рамки
        self.schema_frame = LabelFrame(self, text='JSONSchema', padx=25, pady=20, font='Consolas 20')
        # Створюємо об'єкт текстового поля для редагування JSON-схеми
        self.schema_text = Text(self.schema_frame, font='Consolas 30', width=40, height=20, wrap=tk.NONE)
        # Створюємо меню для вікна
        self.create_menu()
        # Створюємо панель інструментів для редагування JSON - схеми
        self.create_toolbar()
        # Створюємо рамку для відображення JSON-схеми
        self.create_schema_frame()

    # Створюємо меню для вікна
    def create_menu(self):
        # Створюємо об'єкт меню
        self.menu = tk.Menu(self)
        # Додаємо пункт меню "Файл"
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Відкрити", font='10', command=self.open_file)
        self.file_menu.add_command(label="Зберегти", font='10', command=self.save_file)
        self.file_menu.add_command(label="Зберегти як...", font='10', command=self.save_as_file)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Встановлюємо меню для вікна
        self.config(menu=self.menu)

    # Створюємо панель інструментів для редагування JSON-схеми
    def create_schema_frame(self):
        # Розташовуємо текстове поле у рамці
        self.schema_text.pack(fill=BOTH, expand=True)
        # Розташовуємо рамку у лівій частині вікна
        self.schema_frame.pack(side=LEFT, fill=BOTH, expand=True)

    def create_toolbar(self):
        # Створюємо об'єкт панелі інструментів
        self.toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=TOP, fill=tk.X)

    def on_closing(self):
        # Виконайте необхідну дію тут
        self.json_schema_service.auto_save(self.schema_text, self.opened_file)
        self.destroy()
        print("close")

    def open_file(self):
        self.opened_file = self.json_schema_service.open_file(self.schema_text)
        print(self.opened_file)

    def save_file(self):
        print("save file" + self.opened_file)
        self.json_schema_service.save_file(self.schema_text, self.opened_file)
        self.opened_file = ''

    def save_as_file(self):
        self.json_schema_service.save_as_file(self.schema_text)
        self.opened_file = ''
