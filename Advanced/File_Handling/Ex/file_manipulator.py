import os


def file_manipulator():
    while True:
        line = input()
        if line == 'End':
            break

        elif line.startswith('Create'):
            command, file_name = line.split('-')
            with open(f'./{file_name}', 'w') as file:
                pass

        elif line.startswith('Add'):
            command, file_name, content = line.split('-')
            with open(f'./{file_name}', 'a') as file:
                file.write(f'{content}\n')

        elif line.startswith('Replace'):
            command, file_name, old_string, new_string = line.split('-')
            try:
                with open(f'./{file_name}', 'r+') as file:
                    file_content = file.read()
                    if old_string in file_content:
                        file_content = file_content.replace(old_string, new_string)
                    file.seek(0)
                    file.truncate(0)
                    file.write(file_content)

            except FileNotFoundError:
                print('An error occurred')
                continue

        elif line.startswith('Delete'):
            command, file_name = line.split('-')
            try:
                os.remove(f'./{file_name}')
            except FileNotFoundError:
                print('An error occurred')
                continue


file_manipulator()