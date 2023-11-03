import tkinter as tk
from tkinter import ttk, scrolledtext
import ctypes


# Створюємо клас для нашого додатку
class JSONSchemaView(tk.Tk):
    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()
        # Встановлюємо назву вікна
        self.title("JSON Schema Editor")
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        # Встановлюємо розмір вікна
        self.geometry("1200x600")
        # Створюємо меню для вікна
        self.create_menu()
        # Створюємо панель іннструментів для редагування JSON - схеми
        self.create_toolbar()
        # Створюємо рамку для відображення JSON-схеми
        self.create_schema_frame()

    # Створюємо меню для вікна
    def create_menu(self):
        # Створюємо об'єкт меню
        self.menu = tk.Menu(self)
        # Додаємо пункт меню "Файл"
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        # self.file_menu.add_command(label="Відкрити", command=self.open_file)
        # self.file_menu.add_command(label="Зберегти", command=self.save_file)
        # self.file_menu.add_command(label="Вийти", command=self.quit)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        # Встановлюємо меню для вікна
        self.config(menu=self.menu)
    
    # Створюємо панель інструментів для редагування JSON-схеми
    def create_schema_frame(self):
        # Створюємо об'єкт рамки
        self.schema_frame = tk.LabelFrame(self, text="JSON-схема", padx=25, pady=20, font='25')
        # Створюємо об'єкт текстового поля з прокруткою для редагування JSON-схеми
        self.schema_text = scrolledtext.ScrolledText(self.schema_frame, width=40, height=20, wrap=tk.NONE)
        # Розташовуємо текстове поле у рамці
        self.schema_text.pack(fill=tk.BOTH, expand=True)
        # Розташовуємо рамку у лівій частині вікна
        self.schema_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_toolbar(self):
        # Створюємо об'єкт панелі інструментів
        self.toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
