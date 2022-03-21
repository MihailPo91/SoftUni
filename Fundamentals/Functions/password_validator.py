def password_length(password):
    is_lenghty = False
    if 6 <= len(password) <= 10:
        return is_lenghty is True
    else:
        print("Password must be between 6 and 10 characters")


def password_chars(password):
    is_char = False
    ascii_list_num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    ascii_list_letter = list(range(65, 122))
    for el in password:
        if ord(el) not in ascii_list_num and ord(el) not in ascii_list_letter:
            print("Password must consist only of letters and digits")
        else:
            return is_char is True


def password_digits(password):
    digits_counter = 0
    is_digits = False
    ascii_list_num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    for el in password:
        if ord(el) in ascii_list_num:
            digits_counter += 1
            if digits_counter > 2:
                return is_digits is True
        else:
            pass
    if digits_counter < 2:
        print("Password must have at least 2 digits")


user_pass = list(input())
is_lenghty = False
is_char = False
is_digits = False
password_digits(user_pass)
password_chars(user_pass)
password_length(user_pass)

if is_lenghty and is_char and is_digits:
    print("Password is valid")



