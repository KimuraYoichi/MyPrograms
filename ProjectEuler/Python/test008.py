def circulatenumber(n):
    ciculatenumbers = [n]
    firstnumber = 0
    l = [int(x) for x in list(str(n))]
    for j in range(len(l)-1):
        firstnumber = l.pop(0)
        l.append(firstnumber)
        l1 = map(str, l)
        l2 = "".join(l1)
        ciculatenumbers.append(int(l2))
        print(ciculatenumbers)
    return ciculatenumbers

print(circulatenumber(2345))



