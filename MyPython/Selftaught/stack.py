#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:08:47 2019

@author: zx7y-kmr
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple')) # 2
print(fruits.count('tangerine')) # 0

print(fruits.index('banana')) #3

print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
