"""
d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.
"""

import myeuler as mye
import numpy as np

"""
与えられた数のそれぞれの約数を求める　----> [primesum]  真の約数であること。
"""

divisor = []
divisorwork = []
primes = []
n = 10

# for i in range(1,n):
#     primes.append(mye.PrimeFactorization(i).primedivisor())

for i in range(1,n):
    for j in range(1,i-1):
        if i%j == 0:
            divisorwork.append(j)
    divisor.append(divisorwork)
    divisortwork = []

print(divisor)
print(type(divisor))



# """
# 約数の和を求める。
# """
#
# primesum = []
# for i in range(len(primes)):
#     primesum.append(sum(primes[i]))
#
# print(len(primes))
#
#
# yuaisu = []
#
# for i in range(len(primes)):
#     if primesum[i] < n:
#         if primesum[primesum[i]]  == i:
#             yuaisu.append([i,primesum[primesum[i]]])

# print(primes)
# print(primesum[219])
# print(primes[219])
# print(primesum[283])
#
# print(primesum)
# print(yuaisu)

# """
# 約数の重複をなくす。
# """
# primesum_1 = []
#
# primesum_1 = list(set(primesum))
#
# """
# 同一の和を持つ、primes1 の　index のリストを作る。
# """
#
# indexs = []
# for ps in primesum_1:
#     l = [i for i, x in enumerate(primesum) if (x == ps and primesum.count(x) > 1)]
#     if l != []:
#         indexs.append(l)
#
# # print(primes1[indexs[0][0]])
# # print(primes1[indexs[0][1]])
#
# yuailist = []
# for li in indexs:
#     for n in range(len(li)):
#         yuailist.append(primes1[li[n]])
#
# yuaisulist = []
# yuaisu = 1
# for yli in yuailist:
#     for i in range(len(yli)):
#         yuaisu *= yli[i]
#     yuaisulist.append(yuaisu)
#     yuaisu = 1
#
# print(yuailist)
# print(yuaisulist)
# print(sum(yuaisulist))
#
# # print(primes)
# # print(primes1)
# # print(primesum)
# # print(primesum_1)
# # print(indexs)
#
#
#
# # primesum.append(sum(mye.PrimeFactorization(i).primedivisor()))

"""
[priimesum] の要素で同一の要素のインデックスを求める。　index ---> index-1 が元の数
"""

# for ps in primesum:
#     indexs.append([i for i, x in enumerate(primesum) if (x == ps and primesum.count(x) > 1)])

# print(primesum)
# print([i for i, x in enumerate(primesum) if x == 5])
#
# print(indexs)


# print(primesum)
# print(max(primesum))
# l = []
#
# for ps in range(max(primesum)+1):
#     if [x for x in primesum if primesum[x] == ps] is not None:
#         l.append([i for i, x in primesum if primesum[x] == ps])
#
# print(l)


# primesum_dup = sorted([x for x in primesum if primesum.count(x) > 1])
# primesum_dup_unique = list(set(primesum_dup))
# print(primesum_dup_unique)


# [i for i, x in enumerate(l_dup) if x == 'b']
# test =[i for i, x in enumerate(primesum) if primesum.count(x) > 1]
# print(test)
