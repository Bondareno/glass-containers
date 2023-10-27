import os
import time

def count_files(path):
    start_time = time.time()
    file_counter = 0

    for _, _, files in os.walk(path):
        file_counter += len(files)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return file_counter, elapsed_time

if __name__ == "__main__":
    path = os.path.abspath(os.sep)
    total_files, elapsed_time = count_files(path)
    print(f"Total files on your hard drive: {total_files}")
    print(f"Program execution time: {elapsed_time:.2f} seconds")
