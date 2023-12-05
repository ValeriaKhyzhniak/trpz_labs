from app.repositories.I_json_schema_repository import IJSONSchemaRepository
from app.models.json_schema import JSONSchema


class JSONSchemaRepository(IJSONSchemaRepository):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        # Створюємо курсор для БД
        self.cursor = connection.cursor()
        # Створюємо таблицю json_schemas якщо її не існує
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS json_schemas (
            json_id INTEGER PRIMARY KEY,
            json_name text,
            json_data text,
            json_file_path text
        )""")
        connection.commit()

    def get_by_id(self, json_id):
        # Знаходимо елемент із заданою id
        self.cursor.execute("SELECT * FROM json_schemas WHERE json_id=?", (json_id,))
        # Записуємо його в результат
        result = self.cursor.fetchone()
        if result:
            # Повертаємо знайдений елемент
            return JSONSchema(result[0], result[1], result[2], result[3])
        else:
            return None

    def _insert(self, json_schema):
        self.cursor.execute("INSERT INTO json_schemas (json_id, json_name, json_data, json_file_path) VALUES (?, ?, ?, ?)"
                            , (json_schema.json_id, json_schema.json_name, json_schema.json_data,
                               json_schema.json_file_path,))
        self.connection.commit()

    def _update(self, json_schema):
        self.cursor.execute("UPDATE json_schemas SET json_name=?, json_data=?, json_file_path=? WHERE json_id=?",
                            (json_schema.json_name, json_schema.json_data, json_schema.json_file_path,
                             json_schema.json_id))
        self.connection.commit()

    def delete_by_id(self, json_id):
        self.cursor.execute("DELETE FROM json_schemas WHERE json_id=?", (json_id,))
        self.connection.commit()

    def get_by_name(self, json_name):
        self.cursor.execute("SELECT * FROM json_schemas WHERE json_name=?", (json_name,))
        result = self.cursor.fetchone()
        if result:
            return JSONSchema(result[0], result[1], result[2], result[3])
        else:
            return None
