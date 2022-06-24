def flights(*args):
    statistics = {}
    passengers = 0
    destination = ''

    for i, item in enumerate(args):
        if str(item).isdigit():
            continue
        else:
            destination = item
            if i < len(args) - 1:
                passengers = args[i + 1]
            if destination == 'Finish':
                break
            if destination not in statistics:
                statistics[destination] = passengers
            else:
                statistics[destination] += passengers

    return statistics


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))