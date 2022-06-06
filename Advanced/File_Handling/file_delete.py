import os

file_path = './my_first_file'

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')