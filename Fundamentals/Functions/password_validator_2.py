def password_validator(password):
    valid = True

    if len(password) > 10 or len(password) < 6:
        valid = False
        print("Password must be between 6 and 10 characters")

    ascii_list_num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    ascii_list_letter = list(range(65, 122))

    for el in password:
        if ord(el) not in ascii_list_num and ord(el) not in ascii_list_letter:
            valid = False
            print("Password must consist only of letters and digits")
            break

    digits_counter = 0
    for el in password:
        if ord(el) in ascii_list_num:
            digits_counter += 1
            if digits_counter == 2:
                break
    if digits_counter < 2:
        valid = False
        print("Password must have at least 2 digits")

    if valid:
        print("Password is valid")


user_pass = list(input())
password_validator(user_pass)
