#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:06:54 2019

@author: zx7y-kmr
"""
"""
2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.

では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
"""

def soinsubunkai(n):
    soinsu=[]
    for i in range(2,n):
        while n%i==0:
            soinsu.append(i)
            n=int(n/i)
    if n > 1:
        soinsu.append(n)
    return soinsu

yakusu0=[]
n=15

for j in range(2,n+1):
    yakusu0.append(soinsubunkai(j))
    
print(yakusu0)
print("---------")

yakusuMaxList=[]
j=0

    
for i in range(2,n+1):
    for l in yakusu0:
        if l.count(i) > 0:
            if l.count(i) >= j:
                j = l.count(i)
    yakusuMaxList.append([i,j])
    j = 0
            
print(yakusuMaxList)

answer=1

for l in yakusuMaxList:
    answer *= l[0]**l[1]
    
print(answer)
    

        
        
        


            
        
        
    
    