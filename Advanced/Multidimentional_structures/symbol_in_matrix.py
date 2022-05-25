def is_symbol_found(matrix, symbol):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == symbol:
                return i, j
    return None


n = int(input())
matrix = [[ord(x) for x in input()] for _ in range(n)]
symbol_to_find = ord(input())

result = is_symbol_found(matrix, symbol_to_find)

if result:
    row_index, column_index = result
    print(f'({row_index}, {column_index})')
else:
    print(f'{chr(symbol_to_find)} does not occur in the matrix')
