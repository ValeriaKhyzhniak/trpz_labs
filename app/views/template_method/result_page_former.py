from abc import ABC, abstractmethod
from tkinter import *
import ctypes


class ResultPageFormer(ABC):
    def execute(self, text):
        root = self.open_result_page()
        self.create_page_content(root, text)

    def open_result_page(self):
        # Створюємо нове вікно
        root = Tk()
        # Додаємо заголовок вікна
        root.title("JSON Editor")
        # Встановлюємо розмір вікна
        root.geometry("750x500")
        # Встановлюємо DPI-свідомість процесу в Windows, для того щоб програма могла змінювати
        # масштаб елементів інтерфейсу користувача, щоб вони виглядали на екрані більш чітко
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        return root

    @abstractmethod
    def create_page_content(self, root, text):
        pass
