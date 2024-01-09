import os
import time
import sqlite3

def count_files_sqlite(database_path):
    start_time = time.time()
    file_counter = 0

    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Execute SQL query to count files
    cursor.execute("SELECT COUNT(*) FROM files_info")
    result = cursor.fetchone()

    if result:
        file_counter = result[0]

    conn.close()

    end_time = time.time()
    elapsed_time = end_time - start_time

    return file_counter, elapsed_time

if __name__ == "__main__":
    database_path = '/Users/ekaterinabondarenko/Documents/GitHub/glass-containers'  
    total_files, elapsed_time = count_files_sqlite(database_path)
    print(f"Total files in your database: {total_files}")
    print(f"Program execution time: {elapsed_time:.2f} seconds")
