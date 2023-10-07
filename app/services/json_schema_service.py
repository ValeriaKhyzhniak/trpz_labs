import tkinter as tk
from tkinter.filedialog import *
from I_json_schema_service import IJSONSchemaService
from app.repositories.I_json_schema_repository import IJSONSchemaRepository


class JSONSchemaService(tk.Tk, IJSONSchemaService):
    def __init__(self, schema_repository: IJSONSchemaRepository):
        super().__init__()
        self.schema_repository = schema_repository

    def open_file(self):

        op = askopenfilename()
        print(op)
        f = open(op, "r", encoding="utf-8")
        content = f.read()
        self.scema_text.delete(1.0, tk.END)
        self.insert(tk.END, content)

    def save_file(self):
        pass

    def auto_save(self):
        pass

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
