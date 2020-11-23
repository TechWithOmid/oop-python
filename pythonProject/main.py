class Counter:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration


myCounter = Counter(5, 20, 2)

for i in myCounter:
    print(i)

for i in Counter(5, 30, 5):
    print(i)
