import os
import time

def get_top_10_extensions(path):
    start_time = time.time()
    ext_dictionary = dict()
    ext_dictionary['NoExtension'] = 0

    for root, _, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            ext = os.path.splitext(filename)[-1].lower()
            if not ext:
                ext = 'NoExtension'
            ext_dictionary[ext] = ext_dictionary.get(ext, 0) + 1

    top_10_extensions_list = sorted(ext_dictionary.items(), key=lambda x: x[1], reverse=True)[:10]

    for i, (extension, count) in enumerate(top_10_extensions_list, start=1):
        print(f"{i}. Extension: {extension}, Count: {count}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time

if __name__ == "__main__":
    root_path = os.path.abspath(os.sep)
    elapsed_time = get_top_10_extensions(root_path)
    print(f"Program execution time: {elapsed_time:.2f} seconds")
