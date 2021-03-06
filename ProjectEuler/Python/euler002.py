#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:24:55 2019

@author: zx7y-kmr
"""
from typing import Any, Union

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
数列の項の値が400万以下の, 偶数値の項の総和を求めよ.
"""

n1 = 1
n2 = 2
fib = [1, 2]
fibEve = [2]

sumFibEve = 2

limitNumber = 4000000

while True:
    n = n1 + n2
    fib.append(n)
    if n > limitNumber:
        break
    elif n % 2 == 0:
        sumFibEve += n
        fibEve.append(n)
    n1 = n2
    n2 = n

print(sumFibEve)
print(fib)
print(fibEve)
