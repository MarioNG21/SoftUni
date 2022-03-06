class RangeIter(object):
    def __init__(self, start, end):
        self.end = end
        self.start = start
        self.current_num = self.start

    def __next__(self):
        if self.current_num > self.end:
            raise StopIteration

        value = self.current_num
        self.current_num += 1

        return value


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_num = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num > self.end:
            raise StopIteration

        value = self.current_num
        self.current_num += 1

        return value


one_to_ten = custom_range(1, 4)

for x in one_to_ten:
    print(f"--- Outer loop - {x} ---")
    for y in one_to_ten:
        print(f"--- Inner loop - {y} ---")
