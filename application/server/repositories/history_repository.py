from interface_history_repository import InterfaceHistoryRepository
from application.server.models.json_history import JSONHistory


class HistoryRepository(InterfaceHistoryRepository):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        # Створюємо курсор для БД
        self.cursor = connection.cursor()
        # Створюємо таблицю json_schemas якщо її не існує
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS json_histories (
                    history_id INTEGER PRIMARY KEY,
                    json_id INTEGER,
                    date_of_saving DATE,
                )""")
        connection.commit()

    def delete_all(self):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM json_histories')
        self.connection.commit()

    def get_by_id(self, history_id):
        # Знаходимо елемент із заданою id
        self.cursor.execute("SELECT * FROM json_histories WHERE history_id=?", (history_id,))
        # Записуємо його в результат
        result = self.cursor.fetchone()
        if result:
            # Повертаємо знайдений елемент
            return JSONHistory(result[0], result[1], result[2])
        else:
            return None

    def _insert(self, json_history):
        self.cursor.execute(
            "INSERT INTO json_histories (history_id, json_id, date_of_saving) VALUES (?, ?, ?)"
            , (json_history.history_id, json_history.json_id, json_history.date_of_saving))
        self.connection.commit()

    def delete_by_id(self, history_id):
        self.cursor.execute("DELETE FROM json_histories WHERE history_id=?", (history_id,))
        self.connection.commit()

    def _update(self, json_history):
        self.cursor.execute("UPDATE json_histories SET json_id=?, date_of_saving=? WHERE history_id=?",
                            (json_history.json_id, json_history.date_of_saving, json_history.history_id))
        self.connection.commit()
