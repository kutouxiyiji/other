
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:01:07 2017

@author: Kutouxyiji

Question 2
"""

import pandas as pd
import numpy as np
from scipy.stats import linregress


def isNotNaN(num):
    if num != num:
        return(False)
    else:
        return(True)

def IdYear(str1): #identify the year
    str2='???'
    i = 0
    while i <len(str1):
        if str1[i]=='2':
            str2 = str(str1[i:])
        i +=1
    return(str2)

def CountByYear(path,filename):
    df = pd.read_csv(path + filename, sep=',',  engine = "python",encoding="utf-8-sig")

    NumByYear = {}

    j = 2005
    while j<2015:
        NumByYear[str(j)] = 0
        j+=1
    NumByYear['other'] = 0
    for i in range(len(df)):

        a = df['Accident_Index'][i]
        if a[:4] == '2005':
            NumByYear['2005'] +=1
        elif a[:4] == '2006':
            NumByYear['2006'] +=1
        elif a[:4] == '2007':
            NumByYear['2007'] +=1
        elif a[:4] == '2008':
            NumByYear['2008'] +=1
        elif a[:4] == '2009':
            NumByYear['2009'] +=1
        elif a[:4] == '2010':
            NumByYear['2010'] +=1
        elif a[:4] == '2011':
            NumByYear['2011'] +=1
        elif a[:4] == '2012':
            NumByYear['2012'] +=1
        elif a[:4] == '2013':
            NumByYear['2013'] +=1
        elif a[:4] == '2014':
            NumByYear['2014'] +=1
        else:
            NumByYear['other'] +=1
    x=[]
    y=[]
    for i in range(len(NumByYear)-1):
        x.append(2005+i)
        y.append(NumByYear[str(2005+i)])
    print(NumByYear)
    print(linregress(x,y))

    
if __name__ == '__main__':
    path = "C:/Users/Kutouxyiji/Desktop/Python/data incubator/"
    filename2 = "Accidents0514.csv"
    filename = "Casualties0514.csv"
    CountByYear(path,filename)
    
