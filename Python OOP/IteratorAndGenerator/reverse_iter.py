class reverse_iter:
    def __init__(self, iterable):
        self.iterable_list = list(iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.index) > len(self.iterable_list):
            raise StopIteration
        value_to_return = self.iterable_list[self.index]
        self.index -= 1

        return value_to_return


for item in reverse_iter([1, 2, 3, 4]):
    print(item)

for item in reverse_iter({1, 2, 3, 4}):
    print(item)
