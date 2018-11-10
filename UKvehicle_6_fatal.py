# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 02:49:36 2017

@author: Kutouxyiji
"""
import pandas as pd
import numpy as np


def Fatal(path,filename2,filename3):
    df2 = pd.read_csv(path + filename2, sep=',',  engine = "python",encoding="utf-8-sig")
    df3 = pd.read_csv(path + filename3, sep=',',  engine = "python",encoding="utf-8-sig")
    length = min(len(df2),len(df3))
    data = {}
    data['M'] = data['F'] = data['FatalM'] = data['FatalF'] = 0
    for i in range(length):
        if df3['Sex_of_Driver'][i] == 1 : #male
            data['M'] +=1
            if df2['Casualty_Severity'][i] == 1: #fatal
                data['FatalM'] +=1
        if df3['Sex_of_Driver'][i] == 2 : #female
            data['F'] +=1
            if df2['Casualty_Severity'][i] == 1: #fatal
                data['FatalF'] +=1
    print(data)
    p_M = float(data['FatalM'])/float(data['M'])
    p_F = float(data['FatalF'])/float(data['F'])
    return(format(float(p_M)/float(p_F),'.16f'))



if __name__ == '__main__':
    path = "C:/Users/Kutouxyiji/Desktop/Python/data incubator/"
    filename = "Accidents0514.csv"
    filename2 = "Casualties0514.csv"
    filename3 = "Vehicles0514.csv"
    print(Fatal(path,filename2,filename3))