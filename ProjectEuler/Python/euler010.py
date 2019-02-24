#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:13:42 2019

@author: zx7y-kmr

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.

200万以下の全ての素数の和を求めよ.
"""


def primeJudge(n):
    """
    judge n is prime nuber or not
    :param n:
    :return: prime number -> True   not prime number -> False
    """
    found = False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            found = True
            break
        else:
            continue
    if found:
        return False
    else:
        return True


n = 2000000
sosuSum = 0

seqToN = list(range(2, n + 1))

for i in seqToN:
    if i < n and primeJudge(i):
        sosuSum += i
        print(i)

print(sosuSum)
