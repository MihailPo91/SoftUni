number = int(input())

is_prime_number = True

if number % 2 == 0:
    is_prime_number = False
if number % 3 == 0:
    is_prime_number = False
if number % 5 == 0:
    is_prime_number = False


print(is_prime_number)
