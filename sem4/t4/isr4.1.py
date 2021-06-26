import random

massiv=[]
for i in range(10):
    massiv.append(random.randint(-100, 100))
print("Массив\n", massiv)

def insertionSort(mas = []):
    n = len(mas)
    for i in range(1, n):
        elChange = mas[i]
        k = i - 1
        while ((k >= 0)&(mas[k] > elChange)):
            mas[k + 1] = mas[k]
            k -= 1
        mas[k + 1] = elChange
    return mas

print("Сортировка методом вставки\n", insertionSort(massiv))

mas_sort = sorted(massiv)
print("Сортировка с помощью встроенных функций языка\n", mas_sort)
