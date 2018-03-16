# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:16:04 2018
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
@author: Li Ruosong
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence :
            return False
        if len(sequence) == 1:
            return True
        key=sequence[-1]
        contrast_flag=0
        cut_flag=0
        for i in range(0,len(sequence)-1) :
            if sequence[i]<key :
                if contrast_flag == 0:
                    continue
                else:
                    return False
            else:
                contrast_flag = 1
                if i == 0:
                    pass
                elif sequence[i-1]<key or i ==len(sequence)-2:
                    cut_flag = i-1
        if  cut_flag == 0 or cut_flag == len(sequence)-2:
            return self.VerifySquenceOfBST(sequence[:-1])
        else:  
            return self.VerifySquenceOfBST(sequence[:cut_flag+1]) and self.VerifySquenceOfBST(sequence[cut_flag+1:-1]) 
S=Solution()
ARRAY=[5,8,7,12,15,14,3]
print(S.VerifySquenceOfBST(ARRAY))
                
