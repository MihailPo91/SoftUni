def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        parity = 0 if key == 'even' else 1
        filtered = [x for x in value if x % 2 == parity]
        result[key] = filtered
    return {key: value for key, value in sorted(result.items(), key=lambda x: -len(x[1]))}


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))



