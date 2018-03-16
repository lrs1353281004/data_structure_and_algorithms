# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:42:21 2018
二进制中1的个数
在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
@author: Li Ruosong
"""
'''
def count_one(num):
    res=0
    while num>0:
        if num & 1 == 1:
            res +=1
        num=num>>1
    return res

print(count_one(3))

def count_1(num):
    return sum([(num>>i & 1 ) for i in range(0,32)  ] )
'''    
def NumberOf1(self, n):
        # write code here
        
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        count += 1
        n = (n - 1) & n
    return count
print(count_1(3))