# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:05:33 2018
操作给定的二叉树，将其变换为源二叉树的镜像。
@author: Li Ruosong
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if  not root :
            return None
        tmp_left = self.Clone_tree(root.left)
        tmp_right= self.Clone_tree(root.right)
        
        root.right = self.Mirror(tmp_left)
        root.left  = self.Mirror(tmp_right)
        return root
    def Clone_tree(self,root):
        if root:
            new_root=TreeNode(root.val)
        else:
            return None
        new_root.left  = self.Clone_tree(root.left)
        new_root.right = self.Clone_tree(root.right)
        return new_root

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root :
            return None
        root.left,root.right=root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
'''
#testing instance
L1=TreeNode(1)
L2=TreeNode(2)
L3=TreeNode(3)
L4=TreeNode(4)
L5=TreeNode(5)
L6=TreeNode(6)

L1.left=L2
L2.left=L3
L3.left=L4
L4.left=L5


 

S=Solution()
S.Mirror(L1)
print(L1.right.val)
