"""
http://kashiyuki.hatenablog.com/entry/2017/03/05/230423
"""

# import math
#
# m = 20
#
# n = math.factorial(m*2)//(math.factorial(m) * math.factorial(m))
#
# print(n)

# import myeuler
#
# pd = myeuler.PrimeFactorization(100)
#
# print(pd.primedivisor())
# # print(pf.primedivisor())

import myeuler as mye

spam = mye.Spam(5,10)
spam.output()

pf = mye.PrimeFactorization(100)
print(pf.primedivisor())

print(mye.Alph2num('kimura').alph2num())

