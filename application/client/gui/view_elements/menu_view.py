from tkinter import *
from application.client.gui.view_elements.button.button_command.button_involker import ButtonInvoker
from application.client.gui.view_elements.button.button_command.open_file_command import OpenFileCommand
from application.client.gui.view_elements.button.button_command.save_file_command import SaveFileCommand


class MenuView:

    def __init__(self):
        super().__init__()

    # Створюємо меню для вікна
    def create_menu(self, window):
        # Створюємо об'єкт меню
        self.menu = Menu()
        # Додаємо пункт меню "Файл"
        self.file_menu = Menu(self.menu)
        open_file_command = OpenFileCommand(window)
        open_file_involker = ButtonInvoker(open_file_command)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Відкрити"
                                   , command=lambda: open_file_involker.invoke())
        save_file_command = SaveFileCommand(window)
        save_file_involker = ButtonInvoker(save_file_command)
        self.file_menu.add_command(label="Зберегти"
                                   , command=lambda: save_file_involker.invoke())
        return self.menu
