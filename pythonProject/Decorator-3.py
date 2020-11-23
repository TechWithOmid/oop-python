from functools import wraps


def show_decorator(is_true):
    def inner_decorator(func):
        @wraps(func)
        def wrapper():
            if is_true:
                func()
            else:
                print('you don\'t have permission')

        return wrapper
    return inner_decorator


@show_decorator(True)
def show_name():
    print('name showed')


show_name()
