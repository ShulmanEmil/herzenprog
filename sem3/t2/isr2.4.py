def main():
    v = int(input("Введите объем:"))
    print(square(v))

def square(v):
    a = pow(v, 1 / 3)
    s = a * a
    return s

main()