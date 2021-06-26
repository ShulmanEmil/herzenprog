#вариант с использованием цикла for..in
mysum=0;
for i in range (1,101):
   mysum=mysum+i
print('Здесь мы используем цикл for ', mysum)

#вариант с ипользованием lambda функций
l = lambda sum_pr: sum(range(sum_pr + 1))
print('Здесь мы используем lambda ', l(100))
