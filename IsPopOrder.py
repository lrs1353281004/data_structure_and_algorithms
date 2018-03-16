# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:35:32 2018
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
@author: Li Ruosong
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not (pushV and popV and len(pushV) == len(popV)):
            return False
        i=0
        top=0
        while pushV:
            key = self.find(pushV,popV[i])
            if not (type(key) == int) :
                return False
            if key >= top :
                del pushV[key]
                if key>0:
                    top = key-1
                else:
                    top = 0
                i += 1
            else:
                return False
        return True
                
    def find(self,stack,node):
        if not stack:
            return False
        for i in range(0,len(stack)):
            if stack[i] == node :
                return i
        return False

S=Solution()
pushV=[1,2,3,4,5]
popV=[4,5,3,1]
print(S.IsPopOrder(pushV,popV))