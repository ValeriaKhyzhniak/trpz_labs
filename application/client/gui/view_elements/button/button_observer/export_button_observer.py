from application.client.gui.view_elements.button.button_observer.observer import Observer
from application.client.gui.view_elements.result_windows.export_result_page_former import ExportResultPageFormer


class ExportButtonObserver(Observer):
    def update(self, message):
        # Створюємо об'єкт класу ValidationResultPageFormer
        result_page_former = ExportResultPageFormer()
        # Викликаємо метод execute()
        result_page_former.execute(message)
