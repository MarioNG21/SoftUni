from math import inf


def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        counter = 0
        result = []
        for i in seq:
            counter += 1
            result.append(i)
            if counter == n:
                return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
