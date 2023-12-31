from application.client.gui.view_elements.pages.edit_page_view_strategy import EditPageViewStrategy
from application.client.gui.view_elements.pages.view_context import ViewContext
from application.client.client import Client
from tkinter import *
import idlelib.colorizer as ic
import idlelib.percolator as ip


class ClientFileService:
    client = Client("localhost", 12345)

    def choose_tab_for_saving(self, application_window):
        try:
            current_index = application_window.index("current")  # Get the index of the current tab
            current_name = application_window.tab(current_index, "text")
            current_tab = application_window.nametowidget(application_window.select())

            # Перевірка наявності вибраної вкладки
            if current_tab:
                self.save_file(current_tab, current_name)
            else:
                print("No tab selected.")
        except Exception as e:
            print(f"Error while saving file: {e}")

    def save_file(self, current_tab, current_name):
        outer_frame = current_tab.winfo_children()[0]
        schema_text = outer_frame.winfo_children()[0]
        file_content = schema_text.get("1.0", END)
        self.client.send_request(f"SAVE_FILE|{file_content}|{current_name}")


    def open_file(self, application_window):
        try:
            # Відправляємо запит на отримання вмісту файлу
            response = self.client.send_request("OPEN_FILE||")
            # Розбиваємо відповідь на шлях та вміст
            content, path = response.split("|", 1)
            # Створюмо сторінку для редагування
            schema_text = ViewContext(EditPageViewStrategy()).view_page_strategy(application_window, path)
            schema_text.delete(1.0, END)

            self.syntax_highlight(schema_text)
            # Вставляємо в редактор значення змінної content
            schema_text.insert(END, content)

        except Exception as e:
            print(f"Error opening file: {e}")

    def syntax_highlight(self, schema_text):
        cdg = ic.ColorDelegator()
        cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
        cdg.tagdefs['KEYWORD'] = {'foreground': 'orange', 'background': '#FFFFFF'}
        cdg.tagdefs['STRING'] = {'foreground': 'green', 'background': '#FFFFFF'}
        return ip.Percolator(schema_text).insertfilter(cdg)
