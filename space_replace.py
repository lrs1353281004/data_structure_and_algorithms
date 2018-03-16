# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:54:12 2018
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
@author: Li Ruosong
"""
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)
        
S=Solution()
str1='we are the world'
res=S.replaceSpace(str1)