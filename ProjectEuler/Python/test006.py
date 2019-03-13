from functools import reduce

# def changedige(n,m,c):
#     l = [int(x) for x in list(str(n))]
#     for i in c:
#         l[i] = m
#     return int(reduce(lambda x, y: x + y,  [str(x) for x in l]))

def changedigt(n, c):
    candiateList = []
    l = [int(x) for x in list(str(n))]
    for m in range(10):
        for i in c:
            l[i] = m
        candiateList.append(int(reduce(lambda x, y:x + y, [str(x) for x in l])))
    return candiateList


n1 = 12345335
c = (2,4,5)

print(changedigt(12345335, (2, 5, 6)))
# l = [int(x) for x in list(str(n))]
# print(l)
# new_n = int(reduce(lambda x, y: x + y, [str(x) for x in l]))
# print(new_n)
