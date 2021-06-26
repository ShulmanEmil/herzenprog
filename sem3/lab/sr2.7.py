a = [1, 1, 0, 0]
b = [1, 0, 1, 0]
f = []
delimiter = "—"
header = "|  A  ||  B  ||  F  |"
print(delimiter * len(header))
print('| F = ((A→B)∧A)↔A∧B |')
print(delimiter * len(header))
print(header)
print(delimiter * len(header))
for i in range(4):
    f.append(
        int(((not (bool(a[i])) or bool(b[i])) and bool(a[i])) == (
            bool(a[i]) and bool(b[i]))))
    res = "|  " + str(a[i]) + "  ||  " + str(b[i]) + "  ||  " + str(
        f[i]) + "  |"
    print(res)
    print(delimiter * len(header))
