#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:50:09 2019

@author: zx7y-kmr
"""

from collections import Counter
print(sorted("Dynasty"))
print(Counter(sorted("Dynasty")))

from collections import defaultdict
def count_characters(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1
    print(count_dict)
    
count_characters("Dynasty")
