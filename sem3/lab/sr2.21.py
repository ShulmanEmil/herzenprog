b = [0, 0, 1, 1]
c = [0, 1, 0, 1]
f = []
delimiter = "—"
header = "|   B   ||   C   ||   F   |"
print(delimiter * len(header))
print('|   F = B∧¬C∨¬(¬B→C∧B↔B)  |')
print(delimiter * len(header))
print(header)
print(delimiter * len(header))
for i in range(4):
    f.append(
        int((bool(b[i]) and not (bool(c[i])))
            or not (not (not (bool(b[i]))) or
                    (bool(c[i]) and bool(b[i])) == bool(b[i]))))
    res = "|   " + str(b[i]) + "   ||   " + str(c[i]) + "   ||   " + str(
        f[i]) + "   |"
    print(res)
    print(delimiter * len(header))
