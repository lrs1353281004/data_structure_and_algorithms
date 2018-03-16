# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 16:21:21 2018
输入一颗二叉树和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
@author: Li Ruosong
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res
'''


class Solution:
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        def FindPathMain(root, path, currentSum):
            currentSum += root.val
            path.append(root)
            isLeaf=(root.left == None and root.right == None)
            if currentSum == expectNumber and isLeaf:
                onePath = []
                for node in path:
                    onePath.append(node.val)
                result.append(onePath)
            else:
                if root.left:
                    FindPathMain(root.left, path, currentSum)
                if root.right:
                    FindPathMain(root.right, path, currentSum)
            path.pop()
        FindPathMain(root, [], 0)
        return result
        
        
L1=TreeNode(5)
L2=TreeNode(6)
L3=TreeNode(7)
L4=TreeNode(10)
L5=TreeNode(3)
L6=TreeNode(10)
L7=TreeNode(4)
L8=TreeNode(1)
L9=TreeNode(1)
L10=TreeNode(7)
L11=TreeNode(-1)

L1.left=L2
L1.right=L3
L2.left=L4
L2.right=L5
L3.left=L6
L3.right=L7
L4.left=L8
L6.left=L9
L7.right=L10
L10.left=L11



S=Solution()
res=S.FindPath(L1,22)
            
            