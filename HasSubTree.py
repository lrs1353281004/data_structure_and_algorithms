# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:38:23 2018
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
@author: Li Ruosong
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
#转字符串 不可行 已验证


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def convert(p):
            if  p:
                return str(p.val)+convert(p.left)+convert(p.right)
            else:
                return ''
        return convert(pRoot2) in convert(pRoot1) if pRoot2 else False
L1=TreeNode(1)
L2=TreeNode(2)
L3=TreeNode(3)
L4=TreeNode(4)
L5=TreeNode(5)
L6=TreeNode(6)
L7=TreeNode(7)
L8=TreeNode(8)
L1.left=L2
L1.right=L3
L2.left=L4
L2.right=L5
L3.left=L6
L3.right=L7
L4.left=L8

M1=TreeNode(2)
M2=TreeNode(4)
M3=TreeNode(5)
M1.left=M2
M1.right=M3

S=Solution()
print(S.HasSubtree(L1,M1))
'''
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if  not (pRoot1 and pRoot2) :
            return False
        result = False
        if (pRoot1.val == pRoot2.val):
            result=self.is_subtree(pRoot1,pRoot2)
        if not result :
            result=self.HasSubtree(pRoot1.left,pRoot2)
        if not result :
            result=self.HasSubtree(pRoot1.right,pRoot2)
        return result
        # write code here
    def is_subtree(self,na,nb):
        if not nb:
            return True
        if not na or na.val != nb.val :
            return False
        return self.is_subtree(na.left,nb.left) and self.is_subtree(na.right,nb.right)
        
#testing instance
L1=TreeNode(1)
L2=TreeNode(2)
L3=TreeNode(3)
L4=TreeNode(4)
L5=TreeNode(5)
L6=TreeNode(6)
L7=TreeNode(7)
L8=TreeNode(8)
L1.left=L2
L1.right=L3
L2.left=L4
L2.right=L5
L3.left=L6
L3.right=L7
L4.left=L8

M1=TreeNode(2)
M2=TreeNode(4)
M3=TreeNode(5)
M1.left=M2
M1.right=M3

S=Solution()
print(S.HasSubtree(L1,M1))     
'''       
#更简洁版本
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
     
    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left,B.left) and self.is_subtree(A.right, B.right)     
L1=TreeNode(1)
L2=TreeNode(2)
L3=TreeNode(3)
L4=TreeNode(4)
L5=TreeNode(5)
L6=TreeNode(6)
L7=TreeNode(7)
L8=TreeNode(8)
L1.left=L2
L1.right=L3
L2.left=L4
L2.right=L5
L3.left=L6
L3.right=L7
L4.left=L8

M1=TreeNode(2)
M2=TreeNode(4)
M3=TreeNode(5)
M1.left=M2
M1.right=M3

S=Solution()
print(S.HasSubtree(L1,M1))     