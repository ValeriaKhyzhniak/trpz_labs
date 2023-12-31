from application.client.gui.view_elements.button.button_observer.observer import Observer
from application.client.gui.view_elements.result_windows.json_to_flatten_view_result_page_former import JSONToFlattenViewResultPageFormer


class FlattenViewButtonObserver(Observer):
    def update(self, message):
        # Створюємо об'єкт класу ValidationResultPageFormer
        result_page_former = JSONToFlattenViewResultPageFormer()
        # Викликаємо метод execute()
        result_page_former.execute(message)
