def separateList(mas = []):
    mas1 = []
    mas2 = []
    for i in mas:
        if (i >= 0):
            mas1 += [i]
        else:
            mas2 += [i]
    return mas1, mas2

a = [4, 5, 56, 1, 43, 909, 12, -13, -5, 3, -17, 2647893, -92826]
print(separateList(a))
