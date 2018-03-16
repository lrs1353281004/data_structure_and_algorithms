# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:29:18 2018
从上往下打印出二叉树的每个节点，同层节点从左至右打印
@author: Li Ruosong
"""
class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root :
            return None
        res=[]
        queue=[root]
        while queue :
            res.append(queue[0].val)
            queue=self.out_queue(queue)
        return res

    def out_queue(self,queue_in):
        if queue_in[0].left :
            queue_in.append(queue_in[0].left)
        if queue_in[0].right :
            queue_in.append(queue_in[0].right)
        del queue_in[0]
        return queue_in
        
        
        # writcode here
L1=TreeNode(1)
L2=TreeNode(2)
L3=TreeNode(3)
L4=TreeNode(4)
L5=TreeNode(5)
L6=TreeNode(6)
L7=TreeNode(7)

L1.left=L2
L1.right=L3
L2.left=L4
L2.right=L5
L3.left=L6
L3.right=L7

S=Solution()
res=S.PrintFromTopToBottom(L1)