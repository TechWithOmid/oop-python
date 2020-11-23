from functools import wraps


def my_decorator(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"function name is {func.__name__}")
        func(*args, **kwargs)

    return wrapper


@my_decorator
def say_hello(name):
    print(f'{name=}')


say_hello('omid')
print(say_hello.__name__)