import os
import csv
import datetime

class Collector:
    def __init__(self, root_path):
        self.root_path = root_path
        self.file_data = []

    def collect_files(self):
        for root, _, files in os.walk(self.root_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_size = os.path.getsize(file_path)
                file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                file_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                file_info = {
                    'Name': filename,
                    'Full Path': file_path,
                    'Size': file_size,
                    'Creation Date': file_creation_time,
                    'Modification Date': file_modification_time
                }
                self.file_data.append(file_info)

    def save_to_csv(self, csv_filename):
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['Name', 'Full Path', 'Size', 'Creation Date', 'Modification Date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for file_info in self.file_data:
                writer.writerow(file_info)

if __name__ == "__main__":
    root_path = os.environ.get('HOME')  # Замените на путь к каталогу, который вы хотите сканировать
    collector = Collector(root_path)
    collector.collect_files()
    csv_filename = 'file_database.csv'  # Имя файла CSV для сохранения данных
    collector.save_to_csv(csv_filename)
    print(f"File database saved to {csv_filename}")
