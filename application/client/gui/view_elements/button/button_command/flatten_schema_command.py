from application.client.gui.view_elements.button.button_command.interface_command import InterfaceCommand
from application.client.client import Client
from tkinter import *


class FlattenSchemaCommand(InterfaceCommand):

    def __init__(self, schema_text):
        super().__init__()
        self.schema_text = schema_text

    def execute(self):
        client = Client("localhost", 12345)
        # Записуємо вміст редактора в змінну
        json_text = self.schema_text.get(1.0, END)
        # Викликаємо метод валідації json
        return client.send_json_to_flatten_view_request(json_text)
