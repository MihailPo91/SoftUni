def get_primes(data):
    result = []
    flag = False
    for num in data:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
            if not flag:
                yield num
            else:
                flag = False


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
