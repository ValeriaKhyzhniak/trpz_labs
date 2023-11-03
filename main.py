# Імпортуємо клас JSONSchemaView з файлу json_schema_view.py
from app.views.json_schema_view import JSONSchemaView

# Створюємо об'єкт додатку
app = JSONSchemaView()


# Запускаємо додаток
app.mainloop()
