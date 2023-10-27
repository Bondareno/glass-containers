import os
import time

def get_10_largest_files(root_path):
    start_time = time.time()
    file_list = []

    for root, _, files in os.walk(root_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_list.append((file_path, file_size))
            except (FileNotFoundError, PermissionError):
                pass

    ten_largest_files = sorted(file_list, key=lambda x: x[1], reverse=True)[:10]

    for i, (file_path, file_size) in enumerate(ten_largest_files, start=1):
        print(f"{i}) File: {file_path}, Size: {file_size} bytes")

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time

if __name__ == "__main__":
    root_path = os.path.abspath(os.sep)
    elapsed_time = get_10_largest_files(root_path)
    print(f"Program execution time: {elapsed_time:.2f} seconds")
