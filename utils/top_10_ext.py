import sqlite3
from os.path import getmtime
from datetime import datetime
from time import time

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.last_update_time = None
        self.top_ten_extensions = None

    def update_data(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT extension, COUNT(*) as n
            FROM index_files
            GROUP BY extension
            ORDER BY n DESC
            LIMIT 10
        """)

        self.top_ten_extensions = cursor.fetchall()
        self.last_update_time = time()

        connection.close()

    def list_top_ten_extensions_n(self):
        current_time = time()
        if self.last_update_time is None or current_time - self.last_update_time >= 2 * 24 * 3600:
            print("Database on files should be updated!")
            self.update_data()

        return self.top_ten_extensions

if __name__ == '__main__':
    db_manager = DatabaseManager("data/index.sqlite")
    top_extensions = db_manager.list_top_ten_extensions_n()
    print(top_extensions)
