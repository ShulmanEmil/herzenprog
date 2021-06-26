a = [1, 1, 1, 1, 0, 0, 0, 0]
b = [1, 1, 0, 0, 1, 1, 0, 0]
c = [1, 0, 1, 0, 1, 0, 1, 0]
f = []
delimiter = "—"
header = "|  A  ||  B  ||  C  ||  F  |"
print(delimiter * len(header))
print('|       F = (A∨B)∧¬C       |')
for i in range(8):
    f.append(int((bool(a[i]) or bool(b[i])) and (not bool(c[i]))))
print(delimiter * len(header))
print(header)
print(delimiter * len(header))
for i in range(8):
    res = "|  " + str(a[i]) + "  ||  " + str(b[i]) + "  ||  " + str(
        c[i]) + "  ||  " + str(f[i]) + "  |"
    print(res)
    print(delimiter * len(header))
