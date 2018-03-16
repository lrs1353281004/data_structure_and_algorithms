# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:05:45 2018
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
@author: Li Ruosong
"""
'''
#基本方法   用两个新数组分别存储奇数和偶数
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) ==0:
            return []
        stack1=[]
        stack2=[]
        for i in range(0,len(array)):
            if array[i] & 1 ==1:
                stack1.append(array[i])
            else:
                stack2.append(array[i])
        for i in range(0,len(stack1)):
            array[i]=stack1[i]
        for i in range(0,len(stack2)):
            array[len(stack1)+i]=stack2[i]

S=Solution()
array1=[6,1]
S.reOrderArray(array1)
'''
'''
链接：https://www.nowcoder.com/questionTerminal/beb5aa231adc45b2a5dcc5b62c93f593
来源：牛客网

* 1.要想保证原有次序，则只能顺次移动或相邻交换。
 * 2.i从左向右遍历，找到第一个偶数。
 * 3.j从i+1开始向后找，直到找到第一个奇数。
 * 4.将[i,...,j-1]的元素整体后移一位，最后将找到的奇数放入i位置，然后i++。
 * 5.終止條件：j向後遍歷查找失敗。
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) ==0:
            return []
        for i in range(0,len(array)):
            if array[i] &1 ==1:
                continue
            flag = 0
            for j in range(i+1,len(array)):
                if array[j] &1 ==1:
                    flag = 1
                    val=array[j]
                    for k in range(j,i,-1):
                        array[k]=array[k-1]
                    array[i]=val
                    break
            if flag == 0:
                return array
        return array
S=Solution()
array1=[1,2,3,4,5,6,7]
S.reOrderArray(array1)                
            


            