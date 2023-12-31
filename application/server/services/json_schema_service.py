import json
from tabulate import tabulate
import os
from tkinter import filedialog
from application.server.services.interface_json_schema_service import InterfaceJSONSchemaService
from pandas import json_normalize


class JSONSchemaService(InterfaceJSONSchemaService):
    def __init__(self):
        super().__init__()

    def open_file(self):
        # Відкриваємо діалогове вікно для вибору файлу
        file = filedialog.askopenfilename()
        # Перевірка, чи користувач не вибрав файл (скасував операцію)
        if not file:
            return None
        try:
            # Перевірка наявності файлу перед відкриттям
            if not os.path.exists(file):
                print(f"File not found: {file}")
                return None
            # Відкриваємо файл та записуємо вміст в змінну content
            with open(file, 'r', encoding="utf-8") as f:
                content = f.read()
                return f"{content}|{file}"
        except Exception as e:
            print(f"Error opening file: {e}")
            return None

    # Зберігаємо зміни у поточному відкритому файлі
    def save_file(self, file_content, file_name):
        try:
            # Відкриваємо файл для запису
            with open(file_name, "w", encoding="utf-8") as file:
                # Записуємо вміст файлу
                file.write(file_content)
            # Повідомлення про успішне збереження
            return "File saved successfully"
        except Exception as e:
            # Обробка помилок при збереженні
            return f"Error saving file: {e}"

    def validate_schema(self, json_text):
        # # Записуємо вміст редактора в змінну
        # json_text = json_text_frame.get(1.0, END)
        try:
            json.loads(json_text)
            return True, "JSON is valid."
        except json.JSONDecodeError as e:
            return False, f"JSON is not valid. Error: {e}"


    def export_schema_as_markdown_table(self, text_content):
        try:
            data_dict = json.loads(text_content)
            table_data = [[key, value] for key, value in data_dict.items()]
            markdown_table = tabulate(table_data, headers=["Key", "Value"], tablefmt="pipe")
            print(markdown_table)
            self.save_editor_content_to_file(markdown_table)
            return "Export markdown_table completed"
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"

    def save_editor_content_to_file(self, editor_content):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                                     filetypes=[("file.md", "*.md"), ("All files", "*.*")])
            if not file_path:
                return
            # Збереження вмісту редактора у вибраному файлі
            with open(file_path, 'w') as file:
                file.write(editor_content)
            print(f"Editor content saved to '{file_path}' successfully.")
        except Exception as e:
            print(f"Error saving editor content to file: {e}")

    def flatten_schema(self, json_text):
        try:
            flat_data = json_normalize(json.loads(json_text))
            json_data = flat_data.to_json(orient='records', lines=True, indent=2)
            return json_data
        except Exception as e:
            return f"JSON is not valid.: {str(e)} Can't make JSON to flat view."


