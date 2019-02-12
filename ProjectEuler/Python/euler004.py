#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:29:21 2019

@author: zx7y-kmr
"""

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
では, 3桁の数の積で表される回文数の最大値を求めよ.
"""
kaibun = []

for i in range(100,999):
    for j in range(100,999):
        product = i*j
        str1=str(product)
        if str1 == str1[::-1]:
            kaibun.append(product)
            
print(max(kaibun))
            

 

        
        
        