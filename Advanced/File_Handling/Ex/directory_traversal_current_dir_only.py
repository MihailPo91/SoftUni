from os import listdir

files = {}

for item in listdir('./'):
    if '.' in item:
        if item.startswith('.'):
            continue
        elif not item.startswith('.'):
            name, extension = item.split('.')

            if extension not in files.keys():
                files[extension] = [name]
            else:
                files[extension].append(name)
    else:
        continue


with open('./report.txt', 'w') as file:
    for key, value in sorted(files.items()):
        file.write(f'.{key}\n')
        for i in sorted(value):
            file.write(f'---{i}.{key}\n')