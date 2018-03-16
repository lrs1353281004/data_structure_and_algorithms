# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:39:11 2018
P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），
则称其为“最大的”。求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
输出“最大的” 点集合， 按照 X 轴从小到大的方式输出，每行两个数字分别代表点的 X 轴和 Y轴。
@author: Li Ruosong
"""
'''
num=5
point_label=[[1,2],[5,3],[4,6],[7,5],[9,0]]
def Max_point(num,point_label):
    if num == 1:
        return point_label
    res=[]
    point_copy=point_label.copy()
    for i in range(0,len(point_label)):
        current_point=point_label[i]
        flag = 0
        del point_label[i]
        for j in range(0,len(point_label)):
            if point_label[j][0]>current_point[0] and point_label[j][1]>current_point[1] :
                flag = 1
                break
        if flag == 0 :
            res.append(current_point)
        point_label=point_copy.copy()
    res.sort()
    return res
res=Max_point(num,point_label)
'''
n=int(input())
ps=[]
for _ in range(n):
    x,y=input().split(' ')
    ps.append([int(x),int(y)])
def Max_point(num,point_label):
    if num == 1:
        return point_label
    res=[]
    point_copy=point_label.copy()
    for i in range(0,len(point_label)):
        current_point=point_label[i]
        flag = 0
        del point_label[i]
        for j in range(0,len(point_label)):
            if point_label[j][0]>current_point[0] and point_label[j][1]>current_point[1] :
                flag = 1
                break
        if flag == 0 :
            res.append(current_point)
        point_label=point_copy.copy()
    res.sort()
    return res
res=Max_point(n,ps)

for i in range(0,len(res)):
    print(str(res[i][0])+' '+str(res[i][1]))
    if i<len(res)-1 :
        print('\n')