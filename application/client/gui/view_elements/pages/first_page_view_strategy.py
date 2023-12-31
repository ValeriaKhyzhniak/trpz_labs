from tkinter import *
from tkinter import ttk
from application.client.gui.view_elements.button.button_command.open_file_command import OpenFileCommand
from application.client.gui.view_elements.button.button_observer.button_subject import ButtonSubject
from application.client.gui.view_elements.button.button_observer.open_file_button_observer import OpenFileButtonObserver
from application.client.gui.view_elements.pages.interface_view_strategy import InterfaceViewStrategy
from application.client.client import Client


class FirstPageViewStrategy(InterfaceViewStrategy):
    client = Client("localhost", 12345)
    font = ('Consolas 20', 18)
    width = 30

    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()

    def create_application_tab_frame(self, application_tab, name):
        # Створіть власний стиль для вкладок
        first_page_frame = ttk.Frame(application_tab)
        first_page_label = Label(first_page_frame, text='Welcome Page', font=self.font)
        first_page_label.pack()
        # Створюємо команду валідації
        open_file_command = OpenFileCommand(application_tab)
        # Додаємо кнопку для валідації JSON-схеми
        self.open_file_button = ButtonSubject(first_page_frame, "Open file", open_file_command)
        # Створюємо спостерігача
        open_file_button_observer = OpenFileButtonObserver()
        # Додаємо спостерігача для
        self.open_file_button.add_observer(open_file_button_observer)

        # create_file_button = Button(first_page_frame, width=self.width, text="Create file...", font=self.font
        #                             # , button_command=lambda: self.create_new_window.create_new_window()
        #                             )
        first_page_frame.pack(fill='both', expand=True)
        # Додаємо вкладку
        application_tab.add(first_page_frame, text=name)
        return application_tab
