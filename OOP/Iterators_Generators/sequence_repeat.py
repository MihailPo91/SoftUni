class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.iterator = len(self.sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number -= 1
        if self.number < 0:
            raise StopIteration
        string_to_return = ''
        string_to_return += self.sequence[self.index]
        self.index += 1
        if self.index == self.iterator:
            self.index = 0

        return string_to_return


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 7)
for item in result:
    print(item, end ='')