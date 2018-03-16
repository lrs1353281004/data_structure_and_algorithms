# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:06:18 2018
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。调用min,pop,push的时间复杂度都是-1
@author: Li Ruosong
"""
class Solution:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack :
            self.min_stack.append(node)
        elif node <= self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
            
    def pop(self):
        # write code here
        if not self.stack :
            return None
        else:
            self.stack.pop()
            self.min_stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
        
    def min(self):
        # write code here
        return self.min_stack[-1]
