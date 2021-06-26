def fib_max(max_num):
    fib_list = [0, 1]
    current_fib = fib_list[-1]
    while (current_fib < max_num):
        fib_list += [fib_list[-2] + fib_list[-1]]
        current_fib = fib_list[-1]
    return fib_list

print(fib_max(28))
