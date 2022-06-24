def get_magic_triangle(size):
    matrix = []
    for floor in range(2, size+1):
        if floor == 2:
            matrix = [[1], [1, 1]]
        else:
            row = matrix[-1]
            new_row = [1] * floor
            for i in range(floor):
                if i == 0 or i == (floor - 1):
                    new_row[i] = 1
                else:
                    new_row[i] = row[i - 1] + row[i]
            matrix.append(new_row)
    return matrix


print(get_magic_triangle(5))