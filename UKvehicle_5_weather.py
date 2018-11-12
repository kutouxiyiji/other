import pandas as pd
import numpy as np


def Weather(path,filename3,filename):
    df = pd.read_csv(path + filename, sep=',',  engine = "python",encoding="utf-8-sig")
    df3 = pd.read_csv(path + filename3, sep=',',  engine = "python",encoding="utf-8-sig")
    length = min(len(df),len(df3))
    data = {}
    data['GoodWea'] = data['BadWea'] = data['SkidInGood'] = data['SkidInBad'] = 0
    for i in range(length):
        if df['Weather_Conditions'][i] == 1 : #good weather
            data['GoodWea'] +=1
            if df3['Skidding_and_Overturning'][i] >0 and df3['Skidding_and_Overturning'][i] <=5:
                data['SkidInGood'] +=1
        if df['Weather_Conditions'][i] == 2 or df['Weather_Conditions'][i] == 3 or df['Weather_Conditions'][i] == 5 or df['Weather_Conditions'][i] == 6: #bad weather
            data['BadWea'] +=1
            if df3['Skidding_and_Overturning'][i] >0 and df3['Skidding_and_Overturning'][i] <=5:
                data['SkidInBad'] +=1
    p1 = float(data['SkidInGood'])/float(data['GoodWea'])
    p2 = float(data['SkidInBad'])/float(data['BadWea'])
    return(format(float(p2)/float(p1),'.16f'))
        
    
if __name__ == '__main__':
    path = "C:/Users/Kutouxyiji/Desktop/Python/data incubator/"
    filename = "Accidents0514.csv"
    filename2 = "Casualties0514.csv"
    filename3 = "Vehicles0514.csv"
    print(Weather(path,filename3,filename))
