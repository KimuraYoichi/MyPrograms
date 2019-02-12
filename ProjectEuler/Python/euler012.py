"""
三角数の数列は自然数の和で表わされ, 7番目の三角数は 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 である. 三角数の最初の10項は:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

となる.

最初の7項について, その約数を列挙すると, 以下のとおり.

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

これから, 7番目の三角数である28は, 5個より多く約数をもつ最初の三角数であることが分かる.

では, 500個より多く約数をもつ最初の三角数はいくつか.
"""

from collections import Counter


def primeFactor(n) :
    primeFactorList = []
    for i in range( 2, n ) :
        while n % i == 0 :
            primeFactorList.append( i )
            n = n / i
        if n == 1 :
            break
    if n > 1 :
        primeFactorList.append( n )
    return primeFactorList


def primeFactorization(primeList) :
    c = Counter( primeList )
    return c


def divisorCounter(count) :
    divisorCon = 1
    for k, v in count.items() :
        divisorCon *= v + 1
    return divisorCon

def traiangleJudge(n) :
    testNum = (1 + (1 + 8 * n) ** 0.5)
    if testNum.is_integer() :
        print( testNum )
        return testNum
    else :
        return False


seqSum = 0
pc = 0

for i in range(1,2**500):
        seqSum += i
        # print( seqSum )
        pf=primeFactor( seqSum )
        pl=primeFactorization( pf )
        pc=divisorCounter( pl )
        if pc > 500:
            print('----------answer')
            # traiangleJudge( seqSum )
            print( i )
            print( seqSum )
            print( pl )
            print( divisorCounter( pl ) )
            print('---------')
            break
        else:
            # print( i )
            continue


# seqSum = (2 ** 500)
# print( seqSum )
# pf = primeFactor( seqSum )
# pl = primeFactorization( pf )
# pc = divisorCounter( pl )
#
# print( '----------answer' )
# print( seqSum )
# print( pl )
# print( divisorCounter( pl ) )
# print( '---------' )
