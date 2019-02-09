#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:47:43 2019

@author: zx7y-kmr
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
print(stack.is_empty())

stack.push(1)
print(stack.is_empty())

print(stack.pop())
print(stack.is_empty())

for i in range(0,6):
    stack.push(i)
    
print(stack.peek())
print(stack.size())

stack1 = Stack()

for c in "Hello":
    stack1.push(c)
    
reverse=""

while stack1.size():
    reverse += stack1.pop()
    
print(reverse)