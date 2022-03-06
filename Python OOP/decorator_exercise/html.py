def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args)
            return f"<{tag}>{result}</{tag}>"

        return wrapper
    return decorator


@tags('div')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " World!"))
