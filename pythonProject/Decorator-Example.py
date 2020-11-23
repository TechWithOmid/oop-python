from functools import wraps


def show_name(char_count):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name) >= char_count:
                func(name)
            elif len(name) < char_count:
                raise ValueError

        return wrapper

    return inner_decorator


@show_name(5)
def name_info(name):
    print(f"{name=}")


name_info('omid z')
