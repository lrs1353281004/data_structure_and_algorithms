# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:01:56 2018

@author: Li Ruosong
牛客网
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
test_array=[[1,2,4,6,7],[2,3,5,7,8],[4,5,6,9,10],[5,7,9,11,15]]
def find_target(array,target):
    bound_row=len(array)
    bound_column=len(array[0])
    row=bound_row-1
    col=0
    while row>-1 and col<bound_column :
        key=array[row][col]
        if key==target:
            return True
        elif key<target:
            col +=1
        else:
            row -=1
    return False
print(find_target(test_array,-1))