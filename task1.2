import csv
import datetime
import os
from os.path import getsize, join

class Collector:
    def __init__(self, directory):
        self.directory = directory
        self.csv_path = os.path.join(os.path.dirname(__file__), "data", "data.csv")

    def collect_file_info(self):
        file_info = []
        for root, _, files in os.walk(self.directory):
            for name in files:
                file_path = join(root, name)
                try:
                    file_size = getsize(file_path)
                    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                    modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    file_info.append([name, file_path, file_size, creation_date, modification_date])
                except (FileNotFoundError, PermissionError):
                    pass
        return file_info

    def create_csv_database(self):
        with open(self.csv_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Name", "Path", "Size", "Creation Date", "Modification Date"]
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for file_data in self.collect_file_info():
                writer.writerow(file_data)

    def get_csv_path(self):
        return self.csv_path

if __name__ == "__main__":
    directory_to_scan = "C:\\"  # Замените на путь к папке, которую вы хотите просканировать
    collector = Collector(directory_to_scan)
    collector.create_csv_database()
    print(f"Database saved to: {collector.get_csv_path()}")
