def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result[name] = age
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    return '\n'.join([f'{key} is {value} years old.' for key, value in sorted_result])


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))