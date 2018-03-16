# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:54:06 2018

@author: Li Ruosong
"""

def str2int(or_str):
    res=0
    if not or_str :
        return None
    for i in range(0,len(or_str)):
        res += (ord(or_str[i])-48)*(10**(len(or_str)-i-1))
    return res

res=str2int('12356')