from application.client.client import Client
from application.client.gui.main_application_window import MainProgramWindow
import tkinter as tk


def start_gui():
    root = tk.Tk()
    # Створюємо об'єкт додатку
    app = MainProgramWindow(root)

    # Запускаємо додаток
    root.mainloop()

if __name__ == "__main__":
    client = Client("localhost", 12345)
    client.connect()
    start_gui()
