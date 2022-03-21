def char_range(first, second):
    for ch in range(ord(first), ord(second)):
        if ch != ord(first) and ch != ord(second):
            print(chr(ch), end=" ")


first_letter = input()
second_letter = input()

char_range(first_letter, second_letter)
