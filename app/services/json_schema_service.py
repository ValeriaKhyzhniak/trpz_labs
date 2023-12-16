from app.repositories.I_json_schema_repository import IJSONSchemaRepository
from app.services.I_json_schema_service import IJSONSchemaService
from tkinter import *
from tkinter.filedialog import *


class JSONSchemaService(IJSONSchemaService):
    def __init__(self, schema_repository: IJSONSchemaRepository):
        super().__init__()
        self.schema_repository = schema_repository

    def open_file(self, schema_text):
        # Відкриваємо діалогове вікно, яке дозволяє користувачеві вибрати файл
        # Записуємо шлях до файлу в змінну
        opened_file = askopenfilename()
        # Відкриваємо файл та записуємо вміст в змінну content
        f = open(opened_file, "r", encoding="utf-8")
        content = f.read()
        # Очищуємо простір вікна редактора
        schema_text.delete(1.0, END)
        # Вставляємо в редактор значення змінної content
        schema_text.insert(END, content)
        # Повертаємо шлях до файлу
        return opened_file

    # Зберігаємо зміни у поточному відкритому файлі
    def save_file(self, schema_text, file_name):
        # Записуємо вміст редактора в змінну
        content = schema_text.get(1.0, END)
        # Відкриваємо файл та записуємо в нього значення змінної
        f = open(file_name, "w", encoding="utf-8")
        f.write(content)
        # Закриваємо файл
        f.close()
        # Очищаємо вікно редактора
        schema_text.delete(1.0, END)

    # Зберігаємо зміни в новий файл
    def save_as_file(self, schema_text):
        # Відкриваємо діалогове вікно, яке дозволяє користувачеві вибрати файл
        # Записуємо шлях до файлу в змінну
        file_to_save = asksaveasfilename()
        # Записуємо вміст редактора в змінну
        content = schema_text.get(1.0, END)
        # Відкриваємо файл та записуємо в нього значення змінної
        f = open(file_to_save, "w", encoding="utf-8")
        f.write(content)
        # Закриваємо файл
        f.close()
        # Очищаємо вікно редактора
        schema_text.delete(1.0, END)

    # Автозбереження при закритті редактора
    def auto_save(self, schema_text, opened_file):
        print("autosave")
        # Викликаємо метод save_file
        self.save_file(schema_text, opened_file)

    def validate_schema(self):
        pass

    def syntax_highlighting(self):
        pass

    def quit(self):
        pass

    def export_schema(self):
        pass

    def flatten_schema(self):
        pass
