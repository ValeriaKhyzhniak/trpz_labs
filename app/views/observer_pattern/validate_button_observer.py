from app.views.observer_pattern.observer import Observer
from tkinter import *


class ValidateButtonObserver(Observer):
    def update(self, message):
        # Викликаємо метод для створення нового вікна
        self.create_validation_result_view_window(message)

    def create_validation_result_view_window(self, message):
        # Створюємо нове вікно
        root = Tk()
        # Додаємо заголовок вікна
        root.title("Вікно з виводом тексту")
        # Створюємо віджет Text для виводу тексту
        text_widget = Text(root, height=10, width=40)
        # Вставляємо текст (результати валідації)
        text_widget.insert(END, message)
        # Встановлюємо режим DISABLED, щоб текст не можна було редагувати
        text_widget.config(state=DISABLED)
        text_widget.pack()
