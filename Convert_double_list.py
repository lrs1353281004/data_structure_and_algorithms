# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:44:22 2018
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
@author: Li Ruosong
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Node_List(self,pRootOfTree):
        if not pRootOfTree :
            return []
        return self.Node_List(pRootOfTree.left)+[pRootOfTree]+self.Node_List(pRootOfTree.right)
    def Convert(self, pRootOfTree):
        # write code here
        res=self.Node_List(pRootOfTree)
        if len(res)==0:
            return None
        if len(res)==1:
            return pRootOfTree
        res[0].left=None
        res[0].right=res[1]
        res[-1].left=res[-2]
        res[-1].right=None
        for i in range(1,len(res)-1):
            res[i].left=res[i-1]
            res[i].right=res[i+1]
        return res[0]

L1=TreeNode(10)
L2=TreeNode(6)
L3=TreeNode(14)
L4=TreeNode(4)
L5=TreeNode(8)
L6=TreeNode(12)
L7=TreeNode(16)

L1.left=L2
L1.right=L3
L2.left=L4
L2.right=L5
L3.left=L6
L3.right=L7

S=Solution()
S.Convert(L1)
