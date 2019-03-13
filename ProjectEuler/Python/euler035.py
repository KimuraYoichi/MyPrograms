"""
Problem 35 「巡回素数」

197は巡回素数と呼ばれる. 桁を回転させたときに得られる数 197, 971, 719 が全て素数だからである.

100未満には巡回素数が13個ある: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, および97である.

100万未満の巡回素数はいくつあるか?

"""

from sympy import isprime

ans = []


def circulatenumber(n):
    ciculatenumbers = [n]
    firstnumber = 0
    l = [int(x) for x in list(str(n))]
    for j in range(len(l) - 1):
        firstnumber = l.pop(0)
        l.append(firstnumber)
        l1 = map(str, l)
        l2 = "".join(l1)
        ciculatenumbers.append(int(l2))
    return ciculatenumbers


for i in range(2, 1000000):
    if isprime(i):
        perlist = circulatenumber(i)
        allprime = True
        for j in perlist:
            if not isprime(j):
                allprime = False
                break
        if allprime:
            ans.append(i)
print(ans)
print(len(ans))

# [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
# 55
