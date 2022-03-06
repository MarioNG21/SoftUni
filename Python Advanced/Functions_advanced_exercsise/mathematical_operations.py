from collections import deque


def math_operations(*args, **kwargs):
    result = kwargs
    args = deque(args)
    while args:
        for ch in result:
            element = args.popleft()
            if ch == 'a':
                result[ch] += element
            elif ch == 's':
                result[ch] -= element
            elif ch == 'd':
                if element == 0:
                    continue
                result[ch] /= element
            else:
                result[ch] *= element
            if not args:
                break
    return result


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
