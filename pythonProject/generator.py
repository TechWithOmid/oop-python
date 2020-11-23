def count_up_to(max):
    count = 0
    while count < max:
        yield count
        count += 1


counter = count_up_to(6)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

