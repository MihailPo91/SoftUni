from os import listdir
from os.path import isdir, join


def directory_traversal(path, files_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            if element == 'venv':
                continue
            directory_traversal(f'{path}/{element}', files_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


result = {}
directory_traversal('./', result)

with open('./report.txt', 'w') as file:
    for key, value in sorted(result.items()):
        file.write(f'.{key}\n')
        for i in sorted(value):
            file.write(f'---{i}.{key}\n')
