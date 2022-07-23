class reverse_iter:
    def __init__(self, values):
        self.values = reversed(values)

    def __iter__(self):
        return iter(self.values)


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)