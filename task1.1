import os
import pandas as pd

class FileCollector:
    def __init__(self, root_path):
        self.root_path = root_path
        self.file_data = []

    def collect_file_data(self):
        for root, dirs, files in os.walk(self.root_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    file_info = {
                        "Name": filename,
                        "Path": file_path,
                        "Size (bytes)": os.path.getsize(file_path),
                        "Date Created": os.path.getctime(file_path),
                        "Date Modified": os.path.getmtime(file_path)
                    }
                    self.file_data.append(file_info)
                except (FileNotFoundError, PermissionError):
                    pass

    def create_csv_database(self, output_file="files_database.csv"):
        if self.file_data:
            df = pd.DataFrame(self.file_data)
            df.to_csv(output_file, index=False)
            print(f"File database saved to {output_file}")
        else:
            print("No file data to save.")

if __name__ == "__main__":
    root_path = input("Enter the root path to scan: ")
    collector = FileCollector(root_path)
    collector.collect_file_data()
    collector.create_csv_database()
