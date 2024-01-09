import os
import time
import sqlite3

def get_10_largest_files(db_path):
    start_time = time.time()
    file_list = []

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT path, size
        FROM index_files
        ORDER BY size DESC
        LIMIT 10
    """)

    ten_largest_files = cursor.fetchall()

    for i, (file_path, file_size) in enumerate(ten_largest_files, start=1):
        print(f"{i}) File: {file_path}, Size: {file_size} bytes")

    connection.close()

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time

if __name__ == "__main__":
    db_path = "data/index.sqlite"
    elapsed_time = get_10_largest_files(db_path)
    print(f"Program execution time: {elapsed_time:.2f} seconds")
