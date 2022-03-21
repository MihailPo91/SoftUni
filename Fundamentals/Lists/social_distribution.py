def distribution(data, minimum):

    for el, number in enumerate(data):
        richest = max(data)
        index_richest = data.index(richest)
        while number + 1 <= minimum <= richest:
            number += 1
            richest -= 1
        data[el] = number
        data[index_richest] = richest

    for el in data:
        if el >= minimum:
            pass
        else:
            return "No equal distribution possible"

    return data


population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
print(distribution(population, minimum_wealth))
