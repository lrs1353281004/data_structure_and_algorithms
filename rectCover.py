# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:55:10 2018
rectCover
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
@author: Li Ruosong
"""
def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    sum1 = 1
    sum2 = 2
    
    for i in range(2,n):
        res  = sum2 + sum1
        sum1 = sum2
        sum2 = res
    return res
