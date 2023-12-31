from application.client.gui.view_elements.button.button_observer.observer import Observer
from application.client.gui.view_elements.result_windows.validation_result_page_former import ValidationResultPageFormer


class ValidateButtonObserver(Observer):
    def update(self, message):
        # Створюємо об'єкт класу ValidationResultPageFormer
        result_page_former = ValidationResultPageFormer()
        # Викликаємо метод execute()
        result_page_former.execute(message)
