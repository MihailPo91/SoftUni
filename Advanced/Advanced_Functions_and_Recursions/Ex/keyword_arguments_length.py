def kwargs_length(**kwargs):
    counter = 0
    for n in kwargs.keys():
        counter += 1
    return counter


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
