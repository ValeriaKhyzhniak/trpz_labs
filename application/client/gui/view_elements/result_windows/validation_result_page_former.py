from application.client.gui.view_elements.result_windows.result_page_former import ResultPageFormer
from tkinter import *


class ValidationResultPageFormer(ResultPageFormer):
    def create_page_content(self, root, message):
        # Створюємо віджет Text для виводу тексту
        text_widget = Text(root, height=20, width=60)
        # Вставляємо текст (результати валідації)
        text_widget.insert(END, message)
        # Встановлюємо режим DISABLED, щоб текст не можна було редагувати
        text_widget.config(state=DISABLED)
        text_widget.pack()
