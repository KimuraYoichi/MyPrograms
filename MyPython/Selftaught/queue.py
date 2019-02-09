#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:18:18 2019

@author: zx7y-kmr
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    
    def size(self):
        return len(self.items)
    
a_queue = Queue()
for i in range(5):
    a_queue.enqueue(i)
    
print(a_queue.size())

while a_queue.size():
    print(a_queue.dequeue())