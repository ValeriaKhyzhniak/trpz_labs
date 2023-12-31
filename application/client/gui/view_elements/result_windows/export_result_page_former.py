from application.client.gui.view_elements.result_windows.result_page_former import ResultPageFormer
from tkinter import *


class ExportResultPageFormer(ResultPageFormer):
    def create_page_content(self, root, message):
        # Create a Text widget for displaying text
        text_widget = Text(root, height=20, width=60)
        text_widget.pack()
        print(type(message))
        print(message)
        text_widget.insert(END, message)
        # Встановлюємо режим DISABLED, щоб текст не можна було редагувати
        text_widget.config(state=DISABLED)



