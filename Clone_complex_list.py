# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:20:38 2018
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
@author: Li Ruosong
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead :
            return None
        new_Head = RandomListNode(pHead.label)
        old_new_dic={pHead : new_Head}
        p=new_Head
        q=pHead.next
        while q != None:
            p.next = RandomListNode(q.label)
            old_new_dic[q]=p.next
            p = p.next
            q = q.next
        p=new_Head
        q=pHead
        while p !=None:
            if q.random:
                p.random = old_new_dic[q.random]
            p = p.next
            q = q.next
        return new_Head
        
            
