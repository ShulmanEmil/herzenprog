class FibIterator:
    def __init__(self, n):
        self.n = n - 1
        self.count = 0
        self.fib_list = [0, 1]

    def __next__(self):
        if self.count == 0 or self.count == 1:
            self.count += 1
            return self.fib_list[self.count - 1]
        elif self.count <= self.n:
            self.fib_list += [self.fib_list[-2] + self.fib_list[-1]]
            self.count += 1
            return self.fib_list[-1]
        else:
            raise StopIteration

def main():
    num = 16
    iterator_init = FibIterator(num)
    list = []
    for i in range(num):
        list += [next(iterator_init)]
    print(list)

main()
