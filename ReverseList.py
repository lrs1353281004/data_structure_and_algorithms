# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:20:22 2018
输入一个链表，反转链表后，输出链表的所有元素。
@author: Li Ruosong
"""
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        res=[]
        while pHead :
            res.append(pHead.val)
            pHead=pHead.next
        for i in range(len(res)-1,1,-1):
            print(res[i])

head = ListNode(1)
L1   = ListNode(2)
L2   = ListNode(3)
L3   = ListNode(4)
L4   = ListNode(5)
L5   = ListNode(6)

head.next=L1
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5

S=Solution()
S.ReverseList(head)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next :
            return pHead
        lastNode=None
        while pHead :
            tmp = pHead.next 
            pHead.next = lastNode
            lastNode = pHead
            pHead = tmp
        return lastNode
        
        
        
        
        
        
        
        