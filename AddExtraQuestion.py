# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:07:31 2018

@author: Li Ruosong
"""

import math
questionNum=5
levelScore=[1.1,2.3,3.4,11,31]
def AddExtraQuestion(questionNum,levelScores):
    #levelScores=levelScore.split(" ")
    sortedScore=sorted(list(map(int,levelScores)))
    differenceList=[1]*len(sortedScore)
    addQuestionNum=0
    for index in range(len(sortedScore)):
        if index==0:
            differenceList[index]=0
        else:
            differenceList[index]=math.floor((sortedScore[index]-sortedScore[index-1])/10)
            if differenceList[index]>1:
                if index+addQuestionNum % 3 != 1:
                    addQuestionNum=addQuestionNum+differenceList[index]
    if (len(sortedScore)+ addQuestionNum) % 3 != 0:
        addQuestionNum=addQuestionNum+3-(len(sortedScore)+ addQuestionNum) % 3
    return addQuestionNum
print(AddExtraQuestion(questionNum,levelScore))

'''
questionNum=input()
levelScore=input()
def Add_question_num(questionNum,levelScore):
    levelScore=levelScore.split(" ")
    levelScore=sorted(map(float,list(levelScore)))
    add_question_num=0
    
    for i in range(0,len(levelScore)):
        
        if i == len(levelScore)-1 :
            flag = (i+add_question_num)%3
            if flag == 0 :
                add_question_num +=2
            elif flag == 1 :
                if levelScore[i]-levelScore[i-1]>20:
                    add_question_num +=4
                else:
                    add_question_num +=1
            elif levelScore[i]-levelScore[i-1]>10:
                add_question_num +=3
            continue
            
        if i==0 or levelScore[i]-levelScore[i-1]<=10 or (i+add_question_num)%3 == 0:
            continue
        elif (i+add_question_num)%3 == 1 and levelScore[i]-levelScore[i-1]>20:
            add_question_num +=2
        else :
            add_question_num +=1
    return add_question_num
print(Add_question_num(questionNum,levelScore))
'''          
        