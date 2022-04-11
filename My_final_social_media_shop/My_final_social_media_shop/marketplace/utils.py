import string
from random import choice


def random_char_generator(size=10):
    char = string.ascii_lowercase + string.digits
    result = ''.join(choice(char) for _ in range(size))
    return result

