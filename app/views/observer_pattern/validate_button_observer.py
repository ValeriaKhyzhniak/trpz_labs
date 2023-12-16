from app.views.observer_pattern.observer import Observer
from app.views.template_method.validation_result_page_former import ValidationResultPageFormer


class ValidateButtonObserver(Observer):
    def update(self, message):
        # Створюємо об'єкт класу ValidationResultPageFormer
        result_page_former = ValidationResultPageFormer()
        # Викликаємо метод execute()
        result_page_former.execute(message)
