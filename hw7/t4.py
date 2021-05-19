import os


def print_files(path: str):
    for (root, dirs, files) in os.walk(path, topdown=True):
        for i in files:
            yield i


def is_format(file_name: str, format):
    s = file_name.rsplit('.', 1)
    if s[1] == format:
        return True
    return False


def print_files_format(path: str, format: str):
    for i in print_files(path):
        if is_format(i, format):
            print(i)


file_path = "New Folder"
for i in print_files(file_path):
    print(i)
print('------------------------')
print_files_format(file_path, 'txtt')
