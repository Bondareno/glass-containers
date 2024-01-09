import os
import sqlite3
import logging
from os.path import join, islink
from datetime import datetime
from filesmeta.common_minion import CommonMinion
from filesmeta.doc_minion import DocMinion
from filesmeta.gru import Gru
from filesmeta.img_minion import ImgMinion
from filesmeta.pdf_minion import PDFMinion

class Collector:
    def __init__(self, gru, path_from='/', sqlite_path='../data/index.sqlite'):
        self.path_from = path_from
        self.sqlite_path = sqlite_path
        self.gru = gru
        self.headers = ["name", "size", "path", "creation_date", "modification_date"]

    def _to_db(f):
        def wrapper(self):
            con = sqlite3.connect(self.sqlite_path)
            cur = con.cursor()
            names = ", ".join(self.headers)
            for rec in f(self):
                names = ", ".join(rec.keys())
                values = list(rec.values())
                try:
                    cur.execute(f"INSERT INTO files ({names}) VALUES ({', '.join('?' * len(rec))})", values)
                except Exception as e:
                    print(e)
                    continue
            con.commit()
            con.close()
        return wrapper

    @_to_db
    def _scan_dir_generator(self):
        for filename in self.filenames:
            file_path = join(self.dirpath, filename)
            if not islink(file_path):
                try:
                    yield self.gru.gru_get_meta_inf(file_path)
                except Exception:
                    logging.exception(f"Error getting {filename} data")
                    continue

    def _write_dir_data(self):
        for self.dirpath, _, self.filenames in os.walk(self.path_from):
            self._scan_dir_generator()

    def create_table(self):
        con = sqlite3.connect(self.sqlite_path)
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS files (
                name TEXT,
                size INTEGER,
                path TEXT,
                creation_date TEXT,
                modification_date TEXT,
                PRIMARY KEY (path)
            )
        ''')
        con.commit()
        con.close()

    def collect(self):
        self.create_table()
        self._write_dir_data()

if __name__ == "__main__":
    gru_instance = Gru()  
    collector = Collector(gru_instance)
    collector.collect()
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
