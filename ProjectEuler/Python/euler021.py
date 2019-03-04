"""
d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.
"""

m = 10000
divisor = []


def divisorlist(n):
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return divisor


divisorsumdic = {}
amicablelist = []

for m in range(1, m + 1):
    divisorsumdic[m] = sum(divisorlist(m))

for i in range(1, m + 1):
    if divisorsumdic[i] > 0 and divisorsumdic[i] < m and divisorsumdic[i] != i:
        if divisorsumdic[divisorsumdic[i]] == i:
            if [divisorsumdic[i], i] not in amicablelist:
                amicablelist.append([i, divisorsumdic[i]])

print(amicablelist)
sumamicablelist = []

for s in amicablelist:
    sumamicablelist.extend(s)

print(sumamicablelist)
print(sum(sumamicablelist))
