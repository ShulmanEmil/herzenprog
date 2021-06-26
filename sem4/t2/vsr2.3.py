import time

def time_decore_func(func):
    print(time.asctime(), end='')
    return func

@time_decore_func
def decore_func():
    print(' - дата и время выполнения этой функции')

decore_func()
