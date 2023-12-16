from app.views.observer_pattern.observer import Observer
from app.views.template_method.json_to_flatten_view_result_page_former import JSONToFlattenViewResultPageFormer


class FlattenViewButtonObserver(Observer):
    def update(self, message):
        # Створюємо об'єкт класу ValidationResultPageFormer
        result_page_former = JSONToFlattenViewResultPageFormer()
        # Викликаємо метод execute()
        result_page_former.execute(message)
