#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:31:45 2019

@author: zx7y-kmr


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.
a**2 + b**2 = c**2

例えば, 3**2 + 4**2 = 9 + 16 = 25 = 5**2 である.

a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
"""

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if b < c and a ** 2 + b ** 2 == c ** 2:
            print([a, b, c])
