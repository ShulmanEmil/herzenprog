def integrate(f, a, b, *, n_iter=1000):
    h = (b - a) / n_iter
    s = 0
    x = a
    while (x <= (b - h)):
        s += f(x)
        x += h
    res = round(h * s, 8)
    return res


def test():
    from math import sin, cos, tan
    assert integrate(sin, 0, 1) == 0.45843599
    assert integrate(cos, 0, 1) == 0.84115962
    assert integrate(tan, 0, 1) == 0.61329398


if __name__ == '__main__':
    test()
    from math import sin
    print(integrate(sin, 0, 1))
