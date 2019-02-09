#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:55:42 2019

@author: zx7y-kmr
"""

from functools import reduce
from operator import add
from operator import sub
from operator import mul

array = [20, 1, 2, 3, 4, 5]

print(reduce(add, array)) # 35
print(reduce(sub, array)) # 5
print(reduce(mul, array)) # 2400

a = [-1, 3, -5, 7, -9]

print(list(map(abs, a)))

a = [-1, 3, -5, 7, -9]

print(list(filter(lambda x: abs(x) > 5, a)))

a = [-1, 3, -5, 7, -9]

print(list(map(abs, a)))