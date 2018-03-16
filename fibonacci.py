# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:12:50 2018

@author: Li Ruosong
"""

def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    sum1 = 0
    sum2 = 1
    
    for i in range(2,n+1):
        res  = sum2 + sum1
        sum1 = sum2
        sum2 = res
    return res

print(Fibonacci(100))
        