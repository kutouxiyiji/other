# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:01:07 2017

@author: Kutouxyiji

Question 2
"""

import pandas as pd
import numpy as np

def isNotNaN(num):
    if num != num:
        return(False)
    else:
        return(True)
        
def TimeSlot(str1): #every accident put into one time slot
    str_time = ''
    if str(':') in str1:
        for i in range(len(str1)):
            if str1[i] == ':':
                str_time = str1[:i]
                break
    return(str_time)
    
def ConvertK(int1): #help convert the number to time slot which is string
    if int1 <10:
        return('0'+str(int1))
    else:
        return(str(int1))

def FatalRatioTime(path,filename,filename2):
    df = pd.read_csv(path + filename, sep=',',  engine = "python")
    df2 = pd.read_csv(path + filename2, sep=',',  engine = "python")
    Time_SUM = {}  #total accidents per time slot
    Time_FatalSUM = {} #total fatal accidents per time slot
    j = 0
    while j < 24:
        Time_SUM[j] = 0
        Time_FatalSUM[j] = 0
        j+=1
    Time_SUM['other'] = Time_FatalSUM['other'] =0
    length = min(len(df),len(df2))
    for i in range(length):
        k = 0
        FLAG = 0 # flag the the missing data
        while k < 24:
            if TimeSlot(str(df['Time'][i])) == ConvertK(k):
                Time_SUM[k] +=1
                FLAG = 1
                if df2['Casualty_Severity'][i] == 1:
                    Time_FatalSUM[k] +=1
            k +=1
        if FLAG == 0:
            Time_SUM['other'] +=1
            if df2['Casualty_Severity'][i] == 1:
                Time_FatalSUM['other'] +=1

    print(Time_SUM)
    print(Time_FatalSUM)
    i = 0
    while i <24:
        if Time_SUM[i] !=0:
            print('the fatal ratio of time slot {} is {}'.format(i,format(float(Time_FatalSUM[i])/float(Time_SUM[i]),'.16f')))
        i +=1

    
if __name__ == '__main__':
    path = "C:/Users/Kutouxyiji/Desktop/Python/data incubator/"
    filename = "Accidents0514.csv"
    filename2 = "Casualties0514.csv"
    FatalRatioTime(path,filename,filename2)
    
