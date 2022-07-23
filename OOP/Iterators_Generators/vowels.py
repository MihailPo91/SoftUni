# With class

class vowels:
    vowel_chars = 'eyuioa'

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            if self.string[self.index].lower() not in self.vowel_chars:
                self.index += 1
                continue

            value_to_return = self.string[self.index]
            self.index += 1
            return value_to_return

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

print()

# With function
def vowels(string):
    for ch in string:
        if ch.lower() in "aoeiuy":
            yield ch


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

print()

# With generator expression, similar to list comprehension
my_string = 'Abcedifuty0o'
print('\n'.join([y for y in (x for x in my_string if x.lower() in "aoeiuy")]))
