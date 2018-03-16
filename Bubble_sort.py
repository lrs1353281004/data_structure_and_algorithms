# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:10:13 2018
冒泡排序
@author: Li Ruosong
"""
def Bubble_sort(array):
    for i in range(0,len(array)-1):
        for j in range(0,len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
#instance
A=[5,2,6,1,3,4,5]
A_sorted=Bubble_sort(A.copy())

            
