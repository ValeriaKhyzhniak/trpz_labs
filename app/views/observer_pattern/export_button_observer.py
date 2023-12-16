from app.views.observer_pattern.observer import Observer
from app.views.template_method.export_result_page_former import ExportResultPageFormer


class ExportButtonObserver(Observer):
    def update(self, message):
        # Створюємо об'єкт класу ValidationResultPageFormer
        result_page_former = ExportResultPageFormer()
        # Викликаємо метод execute()
        result_page_former.execute(message)
