def main():
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
           144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    print(sum_first(lst))
    print(sum_second(lst))

def sum_first(lst = []):
    length = len(lst) // 2
    cutlst = lst[:length]
    return sum(cutlst[::2])

def sum_second(lst = []):
    length = len(lst) // 2
    sumlst, cutlst = sum(lst), lst[:length]
    cutsum  = sum(cutlst[1::2])
    sum2 = sumlst + cutsum
    return sum2
main()