"""
Problem 34 「桁の階乗」

145は面白い数である. 1! + 4! + 5! = 1 + 24 + 120 = 145となる.

各桁の数の階乗の和が自分自身と一致するような数の和を求めよ.

注: 1! = 1 と 2! = 2 は総和に含めてはならない.

"""
import math
from functools import reduce

keta = []

for n in range(1, 100000):
    nketa = math.factorial(9) * n
    if n > len(str(nketa)):
        keta.append(n)
        break

print(keta)  # 7桁の数字より以上になると、9!×n の方が小さくなる。

lmf = []
for m in range(3, 10**(keta[0] - 1)):
    lm = [int(x) for x in str(m)]
    if m == sum(list(map(lambda x:math.factorial(x), lm))):
        lmf.append(m)

print(lmf)
print(sum(lmf))

# [145, 40585]
# 40730
