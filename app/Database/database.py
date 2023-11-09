import sqlite3


class Database:

    @staticmethod
    def database_connection():
        # Повертаємо з'єднання до БД
        return sqlite3.connect("Database.db")
