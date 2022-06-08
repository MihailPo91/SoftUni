result_string = ''

with open('text.txt', 'r') as file:
    line_number = 1
    for line in file:
        line = line.strip('\n')
        letters = 0
        punctuations = 0

        for ch in line:
            if ch.isalpha():
                letters += 1
            elif ch in ',.-!?\'()"[]{}':
                punctuations += 1

        result_string += f'Line {line_number}: {line} ({letters})({punctuations})\n'
        line_number += 1

with open('./output.txt', 'w') as to_file:
    to_file.write(result_string)