#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:56:47 2019

@author: zx7y-kmr
"""

"""
13195 の素因数は 5, 7, 13, 29 である.

600851475143 の素因数のうち最大のものを求めよ.
"""

n=600851475143
#n=13195

yakusu=[]
x=2
y=1

#for i in range(1,n-1):
#    if n%i == 0:
#       yakusu.append(i)


while n > 1:
    if n%x == 0:
        yakusu.append(x)
        n=n/x
    x+=1

print("yasuku list")
print(yakusu)

print("max prime")
print(max(yakusu))

yakusu.remove(min(yakusu))

for i in yakusu:
    y *= i
    
print("Max yakusu")
print(y)

