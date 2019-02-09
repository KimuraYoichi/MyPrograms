#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:15:36 2019

@author: zx7y-kmr
"""

"""
次の1000桁の数字のうち, 隣接する4つの数字の総乗の中で, 最大となる値は, 9 × 9 × 8 × 9 = 5832である.
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

この1000桁の数字から13個の連続する数字を取り出して, それらの総乗を計算する. では、それら総乗のうち、最大となる値はいくらか.

EX 6桁の数123789から5個の連続する数字を取り出す場合, 1*2*3*7*8と2*3*7*8*9の二通りとなり, 後者の2*3*7*8*9=3024が最大の総乗となる.
"""

n=13
productSubstr=1
productList=[]

s1='73167176531330624919225119674426574742355349194934'
s2='96983520312774506326239578318016984801869478851843'
s3='85861560789112949495459501737958331952853208805511'
s4='12540698747158523863050715693290963295227443043557'
s5='66896648950445244523161731856403098711121722383113'
s6='62229893423380308135336276614282806444486645238749'
s7='30358907296290491560440772390713810515859307960866'
s8='70172427121883998797908792274921901699720888093776'
s9='65727333001053367881220235421809751254540594752243'
s10='52584907711670556013604839586446706324415722155397'
s11='53697817977846174064955149290862569321978468622482'
s12='83972241375657056057490261407972968652414535100474'
s13='82166370484403199890008895243450658541227588666881'
s14='16427171479924442928230863465674813919123162824586'
s15='17866458359124566529476545682848912883142607690042'
s16='24219022671055626321111109370544217506941658960408'
s17='07198403850962455444362981230987879927244284909188'
s18='84580156166097919133875499200524063689912560717606'
s19='05886116467109405077541002256983155200055935729725'
s20='71636269561882670428252483600823257530420752963450'

allstr=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17+s18+s19+s20

for i in range(1001-n):
    if ('0' in allstr[i:n+i]):
        continue
    else:
        for c in list(allstr[i:i+n]):
            productSubstr *= int(c)
        productList.append(productSubstr)
        productSubstr = 1

if  productList:
    print(max(productList))
else:
    print("None")
    


    