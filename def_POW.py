# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:19:52 2018
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
@author: Li Ruosong
"""
import time
base     = 1.01
exponent = 420
#usual method
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        res=1
        flag = exponent
        exponent = abs(exponent)
        while exponent !=0 :
            res = res * base 
            exponent -=1
        if flag >0 :
            return res
        else:
            return 1/res
S1=Solution()
time1 = time.clock()
res1 =S1.Power(base ,exponent)
time2 = time.clock()
print('method 1 Result is : %f '%(res1))
print('method 1 running time is: %f' %(time2-time1))

#better method 快速幂
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if base == 0:
            return 1
        flag=exponent
        exponent = abs(exponent)
        res = 1 
        mul = base
        while exponent != 0:
            if (exponent & 1 == 1):
                res *= mul
            mul *=mul
            exponent = exponent >> 1
        if flag >0 :
            return res
        else:
            return 1/res
S2=Solution()
time1 = time.clock()
res2 =S2.Power(base,exponent)
time2 = time.clock()
print('method 2 Result is : %f '%(res2))                
print('method 2 running time is: %f ' %(time2-time1))            