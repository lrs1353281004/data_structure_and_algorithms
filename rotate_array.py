# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:17:07 2018
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
@author: Li Ruosong
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        left  = 0
        right = len(rotateArray)-1
        while right-left>1 :
            mid=int(floor((left+right)/2))
            if rotateArray[mid]==rotateArray[left]==rotateArray[right]:
                return min(rotateArray)
            elif rotateArray[mid]>=rotateArray[left]:
                left=mid
            elif rotateArray[mid]<=rotateArray[right]:
                right=mid
           
                
        return rotateArray[right]
S=Solution()
array=[3,4,1,2,3]
minnum=S.minNumberInRotateArray(array)