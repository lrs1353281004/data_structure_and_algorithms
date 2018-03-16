# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:41:00 2018
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路：
栈A用来作入队列
栈B用来出队列，当栈B为空时，栈A全部出栈到栈B,栈B再出栈（即出队列）
@author: Li Ruosong
"""
class Solution:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB == []:
            while self.stackA :
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        return self.stackB.pop()
        