# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:18:28 2018
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
@author: Li Ruosong
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        '''
        if not pHead1 and not pHead2 :
            return None
        elif not pHead1 :
            return pHead2
        elif not pHead2 :
            return pHead1
        '''
        Head_Node = ListNode(0)
        backup = Head_Node
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val :
                Head_Node.next = pHead1
                pHead1 = pHead1.next
            else:
                Head_Node.next = pHead2
                pHead2 = pHead2.next
            Head_Node = Head_Node.next
        if pHead1:
            Head_Node.next = pHead1
        else:
            Head_Node.next = pHead2
        return backup.next
                
