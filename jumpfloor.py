# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:15:56 2018
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
@author: Li Ruosong

def jumpfloor(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return jumpfloor(n-1)+jumpfloor(n-2)
"""       
def jumpfloor(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    sum1 = 1
    sum2 = 2
    
    for i in range(2,n):
        res  = sum2 + sum1
        sum1 = sum2
        sum2 = res
    return res
print (jumpfloor(100))
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
def jumpfloor(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    cum=3
    
    for i in range(2,n):
        res  = cum
        cum = cum+res
    return res
print(jumpfloor(10))