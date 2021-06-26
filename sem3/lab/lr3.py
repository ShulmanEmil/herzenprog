a = [1, 1, 0, 0]
b = [1, 0, 1, 0]
c = []
delimiter = "-------------------------"
header = "|  A  ||  B  || A and B |"
for i in range(0, 4, 1):
    c.append(int((bool(a[i]) and bool(b[i]))))
print(delimiter)
print(header)
print(delimiter)
for i in range(0, 4, 1):
    res = "|  " + str(a[i]) + "  ||  " + str(b[i]) + "  ||    " + str(
        c[i]) + "    |"
    print(res)
    print(delimiter)
