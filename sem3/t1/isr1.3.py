from math import *

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if a+b<=c or a+c<=b or c+b<=a:
  print("Значения введены неверно!")
else:
  p = (a + b + c)/2
  s = round(sqrt(p*(p-a)*(p-b)*(p-c)), 5)
  print("Результат вычислений равен ", s)