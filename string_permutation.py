# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:08:01 2018
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
@author: Li Ruosong
"""
class Solution:
    def Permutation_order(self,ordered_str):
        if len(ordered_str)<=1:  
            return [ordered_str]  
        RES=[]  
        for i in range(len(ordered_str)): 
            if i<len(ordered_str)-1 and ordered_str[i] == ordered_str[i+1]:
                continue
            for j in self.Permutation_order(ordered_str[0:i]+ordered_str[i+1:]):  
                RES.append(ordered_str[i]+j)  
        return RES  
    def Permutation(self, ss):
        # write code here
        order=[]
        res=[]
        if not ss :
            return res
        if len(ss) == 1:
            return [ss]
        res.append(ss[0])
        for i in range(1,len(ss)):
            if ss[i] <= res[0] :
                res = [ss[i]]+res
            elif ss[i] > res[-1]:
                res = res +[ss[i]]
            else:
                for k in range(1,len(res)):
                    if ss[i]< res[k] :
                        res = res[:k]+[ss[i]]+res[k:]
                        break
                    if ss[i]==res[k] :
                        break
        return self.Permutation_order(''.join(res))
S=Solution()
res=S.Permutation('aabaa')            
'''
def fun1(s=''):  
    if len(s)<=1:  
        return [s]  
    sl=[]  
    for i in range(len(s)):  
        for j in fun1(s[0:i]+s[i+1:]):  
            sl.append(s[i]+j)  
    return sl  

res=fun1('adfn')                 
'''        
        
