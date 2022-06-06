file_path = './text.txt'
# file_path = './text2.txt'

try:
    open(file_path)
    print('File found')
except FileNotFoundError:
    print('File not found')
