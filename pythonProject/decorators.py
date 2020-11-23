# def my_decorator(func):
#     def say_bye():
#         print('bye bye')
#         func()
#
#     return say_bye
#
#
# def say_hello():
#     print('hey')
#
#
# say_hello = my_decorator(say_hello)
# say_hello()

# def my_decorator(func):
#     def say_hello():
#         print("hey")
#         func()
#
#     return say_hello
#
#
# @my_decorator
# def say_bye():
#     print('bye')
#
#
# say_bye()


def my_decorator(func):
    def say_hello(*args, **kwargs):
        print(f'hey')
        func(*args, **kwargs)

    return say_hello


@my_decorator
def say_bye(name):
    print(f'bye {name}')


@my_decorator
def say_info(name, family):
    print(f"{name=} {family=}")


say_bye('omid')
say_info('omid', 'mohammadi')
