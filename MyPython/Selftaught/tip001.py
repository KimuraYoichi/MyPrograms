#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:48:28 2019

@author: zx7y-kmr
"""

print(any((x % 2 == 0 for x in [1,2,3])))
 # => True

print(any((x % 2 == 0 for x in [1,3,5])))

 # => False
print(all((x % 2 == 0 for x in [1,3,5])))

 # => False
print(all((x % 2 == 0 for x in [2,4,6])))
 # => True
 
i = 2049
lst = []
while i > 0:
    lst.append(i%10)
    i //= 10 # 必須
lst.reverse()
print(lst)
# 結果-> [2, 0, 4, 9]