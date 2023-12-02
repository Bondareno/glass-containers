import sqlite3
from filesmeta.common_minion import CommonMinion
from filesmeta.doc_minion import DocMinion
from filesmeta.gru import Gru
from filesmeta.img_minion import ImgMinion
from filesmeta.pdf_minion import PDFMinion
from staff.collector import Collector as OldCollector

class Collector(OldCollector):
    def save_to_sqlite(self, data_info):
        connection = sqlite3.connect(self.sqlite_path)
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                name TEXT,
                size INTEGER,
                path TEXT,
                creation_date TEXT,
                modification_date TEXT,
                PRIMARY KEY (path)
            )
        ''')

        cursor.executemany('''
            INSERT OR REPLACE INTO files
            (name, size, path, creation_date, modification_date)
            VALUES (?, ?, ?, ?, ?)
        ''', data_info)

        connection.commit()
        connection.close()
