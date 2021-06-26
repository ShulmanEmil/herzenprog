import random

def main():
    кфтв = 'yes'
    while(f == 'yes'):
        max_gr = int(input('Введите максимальное число: '))
        min_gr = int(input('Введите минимальное число: '))
        num = int(input('Ваше предположение это число... '))
        rand = random.randrange(min_gr,max_gr, 1);
        search(num, rand)
        print("Начать игру заново?(yes/no)")
        rand = input()

def search(num, finder):
    while num != finder:
        if num < finder:
            print("Число {} меньше, чем искомое".format(str(num)))
            num = int(input('Ваше предположение это число... '))
        else:
            print("Число {} больше чем искомое".format(str(num)))
            num = int(input('Ваше предположение ээто число... '))
    print("Вы угадали!")

main()
