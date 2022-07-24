def solution():

    def integers():
        value = 1
        while True:
            to_return = value
            value += 1
            yield to_return

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        result = []
        for num in seq:
            n -= 1
            if n < 0:
                break
            result.append(num)
        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
