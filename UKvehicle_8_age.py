# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 03:01:39 2017

@author: Kutouxyiji
"""

import pandas as pd
import numpy as np
from pylab import *
from scipy.optimize import curve_fit


def Age(path,filename3):
    df3 = pd.read_csv(path + filename3, sep=',',  engine = "python",encoding="utf-8-sig")
    length = len(df3)
    data = {}
    j = 17
    while j<120:
        data[j] = 0
        j +=1
    for i in range(length):
        if df3['Age_of_Driver'][i] >=17 : #legal
            data[df3['Age_of_Driver'][i]] +=1
    print(data)
    

def func(x, a, b, c):
    return a*np.exp(-b*x)+c

def fit(data):
    x=[]
    y=[]
    for i in range(100):
        x.append(i+17)
        d = int(data[(i+17)])
        y.append(d)
    popt, pcov = curve_fit(func, x, y)

if __name__ == '__main__':
    path = "C:/Users/Kutouxyiji/Desktop/Python/data incubator/"
    filename = "Accidents0514.csv"
    filename2 = "Casualties0514.csv"
    filename3 = "Vehicles0514___TEST.csv"
    data = Age(path,filename3)
    x=[]
    y=[]
    for i in range(100):
        x.append(i+17)
        d = int(data[(i+17)])
        y.append(d)
    popt, pcov = curve_fit(func, x, y)