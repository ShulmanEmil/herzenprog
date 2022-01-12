def integrate(f, a, b, *, n_iter=1000):
    h = (b - a) / n_iter
    s = 0
    x = a
    while (x <= (b - h)):
        s += f(x)
        x += h
    res = round(h * s, 8)
    return res


def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):
    import concurrent.futures as ftres
    from functools import partial
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in ftres.as_completed(fs))


def timer():
    from timeit import timeit
    test105 = timeit(
        "integrate(atan, 0, pi / 2, n_iter=10**5)",
        number=100,
        setup="from __main__ import integrate;  from math import atan, pi")
    test106 = timeit(
        "integrate(atan, 0, pi / 2, n_iter=10**6)",
        number=100,
        setup="from __main__ import integrate;  from math import atan, pi")
    test_async2 = timeit(
        "integrate_async(atan, 0, pi / 2, n_jobs=2, n_iter=10**6)",
        number=100,
        setup="from __main__ import integrate_async;  from math import atan, pi")
    test_async4 = timeit(
        "integrate_async(atan, 0, pi / 2, n_jobs=4, n_iter=10**6)",
        number=100,
        setup="from __main__ import integrate_async;  from math import atan, pi")
    test_async6 = timeit(
        "integrate_async(atan, 0, pi / 2, n_jobs=6, n_iter=10**6)",
        number=100,
        setup="from __main__ import integrate_async;  from math import atan, pi")
    print("test 10^5: ", test105, "\ntest 10^6: ", test106, "\ntest async 2: ", test_async2, "\ntest async 4: ", test_async4, "\ntest async 6: ", test_async6 )


if __name__ == '__main__':
    timer()
