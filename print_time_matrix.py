# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:04:49 2018
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
@author: Li Ruosong
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        new_list=[]
        while matrix :
            new_list.extend(matrix[0])
            matrix=self.TurnMatrix(matrix[1:])
        return new_list
        
    def TurnMatrix(self,matrix):
        if not matrix :
            return []
        or_row_len=len(matrix)
        or_column_len=len(matrix[0])
        turn_matrix=[[0 for i in range(or_row_len)] for j in range(or_column_len)]
        for or_row in range(0,or_row_len):
            for or_col in range(0,or_column_len):
                turn_matrix[or_column_len-or_col-1][or_row] = matrix[or_row][or_col]
        return turn_matrix
            
            
S=Solution()
or_matrix=[[1,2],[3,4],[5,6]]
turn_matrix=S.printMatrix(or_matrix)