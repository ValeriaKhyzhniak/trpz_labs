import json
from app.services.I_json_schema_service import IJSONSchemaService
from tkinter import *
from tkinter.filedialog import *


class JSONSchemaService(IJSONSchemaService):
    def __init__(self):
        super().__init__()
        
    def open_file(self, schema_text):
        # Відкриваємо діалогове вікно, яке дозволяє користувачеві вибрати файл
        # Записуємо шлях до файлу в змінну
        file = askopenfilename()
        # Відкриваємо файл та записуємо вміст в змінну content
        f = open(file, "r", encoding="utf-8")
        content = f.read()
        # Очищуємо простір вікна редактора
        schema_text.delete(1.0, END)
        # Вставляємо в редактор значення змінної content
        schema_text.insert(END, content)
        # Повертаємо шлях до файлу
        return file

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

    def validate_schema(self, json_text_frame):
        # Записуємо вміст редактора в змінну
        json_text = json_text_frame.get(1.0, END)
        try:
            json.loads(json_text)
            return "JSON is valid."
        except json.JSONDecodeError as e:
            return f"JSON is not valid. Error: {e}"

    def syntax_highlighting(self):
        pass

    def quit(self):
        pass

    def export_schema(self):
        pass

    def flatten_schema(self):
        pass
