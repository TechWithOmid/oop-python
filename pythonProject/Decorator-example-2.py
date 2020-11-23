from time import time


def speed_test(func):
    def wrapper(*args, **kwargs):
        start_speed = time()
        func(*args, **kwargs)
        end_speed = time()
        print(f"Time Elapsed: {end_speed - start_speed}")

    return wrapper


@speed_test
def sum_num_gen():
    return sum(x for x in range(5000000))


@speed_test
def sum_num_list():
    return sum([x for x in range(5000000)])


sum_num_gen()
sum_num_list()
