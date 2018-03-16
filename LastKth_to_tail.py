# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:19:51 2018
输入一个链表，输出该链表中倒数第k个结点。
@author: Li Ruosong
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
#返回结点对应值
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head.next :
            return None
        value_list = []
        count_len  = 0
        while head :
            value_list.append(head.val)
            count_len +=1
            head=head.next
        if k > count_len :
            return None
        else:
            return value_list[count_len-k]
        
 '''   
#返回结点
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res_stack = []
        while head :
            res_stack.append(head)
            head=head.next
        if k > len(res_stack) or k<1 :
            return 
        else:
            return res_stack[-k]           

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
print(S.FindKthToTail(head,1))