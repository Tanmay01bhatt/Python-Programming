# Creating a custom class based iterator
# Always use 2 functions:
# 1- __iter__()
# 2 - __next__()


class count:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start = self.start + 1
        return self.start - 1


for x in count(2, 10):
    print(x)
