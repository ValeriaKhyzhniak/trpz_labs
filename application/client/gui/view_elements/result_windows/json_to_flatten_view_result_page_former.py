from application.client.gui.view_elements.result_windows.result_page_former import ResultPageFormer
from tkinter import *


class JSONToFlattenViewResultPageFormer(ResultPageFormer):
    def create_page_content(self, root, json):
        main_frame = LabelFrame(root, text="JSON to flatten view")
        # Створюємо віджет Text для виводу тексту
        text_widget = Text(main_frame, height=20, width=80)
        # Вставляємо текст
        text_widget.insert(END, json)
        # Встановлюємо режим DISABLED, щоб текст не можна було редагувати
        text_widget.config(state=DISABLED)
        text_widget.pack()
        main_frame.pack()
