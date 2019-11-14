class Counter:
    def __init__(self, low, high):
        self.high = high
        self.low = low

    def __iter__(self):
        return self

    def __next__(self):
        if self.low < self.high:
            x = self.low
            self.low += 1
            return x
        raise StopIteration

c = Counter(0, 10)
iter(c)
for i in Counter(0, 10):
    print(i)