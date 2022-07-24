class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.next_value = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter > self.count:
            raise StopIteration
        self.counter += 1
        value_to_return = self.next_value
        self.next_value += self.step
        return value_to_return


numbers = take_skip(2, 6)
for number in numbers:
    print(number)