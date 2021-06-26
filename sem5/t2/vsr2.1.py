import itertools

def fib_numbers(n):
    fib_list = [0, 1]
    for i in itertools.count(0):
        if i > 1:
            fib_list += [fib_list[-2] + fib_list[-1]]
        if i >= n - 1:
            break
    return fib_list

def main():
    n = 28
    print(fib_numbers(n))

main()
