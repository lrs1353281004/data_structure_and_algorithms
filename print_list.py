# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 10:07:56 2018
输入一个链表，从尾到头打印链表每个节点的值。
@author: Li Ruosong
"""
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        item=len(listNode)
        for i in range(item-1,-1,-1):
            print(listNode[i])
S=Solution()
test=[3,5,4,6,5,6]
S.printListFromTailToHead(test)
