from tkinter import ttk, messagebox
import ctypes
from application.client.gui.view_elements.menu_view import MenuView
from application.client.gui.view_elements.pages.first_page_view_strategy import FirstPageViewStrategy
from application.client.gui.view_elements.pages.view_context import ViewContext
from application.client.client_file_service import ClientFileService


# Створюємо клас для нашого додатку
class MainProgramWindow:
    menu_view = MenuView()
    # Ініціалізуємо атрибути класу
    def __init__(self, root):
        super().__init__()
        self.root = root
        # Встановлюємо назву вікна
        self.root.title("JSON Tools")
        # Встановлюємо розмір вікна
        self.root.geometry("1000x600")
        # Встановлюємо DPI-свідомість процесу в Windows, для того щоб програма могла змінювати
        # масштаб елементів інтерфейсу користувача, щоб вони виглядали на екрані більш чітко
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        # Створюємо об'єкт класу Style(), щоб налаштувати власний стиль
        s = ttk.Style()
        # Змінюємо стиль тексту (в параметр font передаємо значення з загального стилю)
        s.configure('TNotebook.Tab', font=("Consolas", 14))
        # Створюємо контейнер, щоб можна було відображати декілька вкладок
        self.application_window = ttk.Notebook(root)
        # Розміщуємо об'єкт на головному вікні
        self.application_window.pack(expand=True, fill="both")
        # Додаємо меню
        self.root.config(menu=self.menu_view.create_menu(self.application_window))
        # Створюємо початкову сторінку
        self.welcome_page = ViewContext(FirstPageViewStrategy()).view_page_strategy(self.application_window, 'General Information')
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        client_file_service = ClientFileService()
        # Викликати метод process_tab_content для кожної вкладки
        for tab_id in self.application_window.tabs():
            current_name = self.application_window.tab(tab_id, "text")
            tab = self.application_window.nametowidget(tab_id)
            if current_name != 'General Information':
                client_file_service.save_file(tab, current_name)
                print(current_name)


            # process_tab_content(tab_id)

        # Показати повідомлення про закриття
        messagebox.showinfo("Закриття програми", "Дякуємо за використання програми!")

        # Закриття вікна
        self.root.destroy()
