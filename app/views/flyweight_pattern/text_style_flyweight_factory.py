from app.views.flyweight_pattern.text_style_flyweight import TextStyleFlyweight


class TextStyleFlyweightFactory:
    # Змінна, яка зберігає в собі список наявних стилів
    _styles = {}

    def get_style(self, font_family, font_size, text_color):
        # Створюємо кортеж, що визначає унікальний ключ для ідентифікації
        # конкретного стилю тексту на основі його властивостей
        key = (font_family, font_size, text_color)
        # Перевіряємо чи стиль з вказаними властивостями вже існує в колекції
        if key not in self._styles:
            # Якщо ні, то створюємо новий екземпляр та додаємо його до списку
            self._styles[key] = TextStyleFlyweight(font_family, font_size, text_color)
        return self._styles[key]
