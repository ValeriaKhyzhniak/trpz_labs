from tkinter import *
from app.views.create_new_page import CreateNewPage
from app.views.strategy.interface_view_strategy import InterfaceViewStrategy


class FirstPageViewStrategy(InterfaceViewStrategy):
    # Створюємо об'єкт класу CreateNewPage()
    create_new_window = CreateNewPage()
    font = ('Consolas 20', 18)
    width = 30

    # Ініціалізуємо атрибути класу
    def __init__(self):
        super().__init__()

    def create_operating_window(self, window):
        # Створіть власний стиль для вкладок
        first_page_frame = Frame(window, width=100, height=700)
        first_page_label = Label(first_page_frame, text='Welcome Page', font=self.font)
        # Створюємо кнопки
        open_file_button = Button(first_page_frame, width=self.width, text="Open file...", font=self.font
                                 , command=lambda: self.create_new_window.open_new_window(window)
                                 )
        create_file_button = Button(first_page_frame, width=self.width, text="Create file...", font=self.font
                                    # , command_pattern=lambda: self.create_new_window.create_new_window()
                                    )
        # Розташовуємо їх
        first_page_label.grid(row=0, column=0)
        open_file_button.grid(row=1, column=0)
        create_file_button.grid(row=2, column=0)
        first_page_frame.pack(fill='both', expand=True)
        # Додаємо вкладку
        window.add(first_page_frame, text='General Information')
        # Розташовуємо вкладку вгорі сторінки
        window.place(relx=0, rely=0, anchor='nw')
        return window
