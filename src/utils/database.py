import sqlite3

class DatabaseManager:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        # Gerekli tabloları oluştur
        pass  # Buraya tablo oluşturma SQL komutlarını yaz

    def execute_query(self, query, parameters=None):
        cursor = self.conn.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor

    def fetch_all(self, query, parameters=None):
        cursor = self.execute_query(query, parameters)
        return cursor.fetchall()

    def fetch_one(self, query, parameters=None):
        cursor = self.execute_query(query, parameters)
        return cursor.fetchone()
