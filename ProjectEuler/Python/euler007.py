#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 17:20:30 2019

@author: zx7y-kmr

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

10 001 番目の素数を求めよ.
"""

n=200000
furui = list(range(2,n+1))
furui1 = list(furui)

for i in furui:
    if i == 2:
        continue
    else:
        for j in range(2,int(i**0.5)+2):
            if i%j==0:
                furui1.remove(i)
                break
print(furui1)
print(len(furui1))
print(furui1[10000])