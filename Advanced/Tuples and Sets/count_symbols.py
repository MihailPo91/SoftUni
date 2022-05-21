text = input()
symbols_counts = {}

for index in range(len(text)):

    if text[index] not in symbols_counts:
        symbols_counts[text[index]] = 0
    symbols_counts[text[index]] += 1

for char, number in sorted(symbols_counts.items()):
    print(f'{char}: {number} time/s')
