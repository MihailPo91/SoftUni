class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                  'X': 10, 'V': 5, 'I': 1}
        numbers = [values[char] for char in value]
        total = 0
        for num1, num2 in zip(numbers, numbers[1:]):
            if num1 >= num2:
                total += num1
            else:
                total -= num1
        return cls((total + num2))

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                return cls(int(value))
            except ValueError:
                return "wrong type"
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
