ll = [1, 2, 3, 4, 5, 6]


def for_loop_recursion(iterable):
    def for_loop_internal(iterable_iter):
        try:
            print(next(iterable_iter))
            for_loop_internal(iterable_iter)
        except StopIteration:
            return

    return for_loop_internal(iter(iterable))

