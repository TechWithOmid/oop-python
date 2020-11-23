# def fib_lit(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums
#
# print(fib_lit(1000))

def fib_gen(max):
    x, y = 0, 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield y
        count += 1


count = fib_gen(1000)
for i in range(0, 1000):
    print(next(count))
