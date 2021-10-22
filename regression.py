import datetime
import pandas as pd
from sklearn import linear_model as lm
import glob
import matplotlib.pyplot as plt


global list2

def saveData(list):
    global list2 
    list2 = []
    list2.append([list])




for file in glob.iglob(r'C:\Users\thomi\PycharmProjects\BigData\Data\*.csv'):
    dataframe = pd.read_csv(file, sep=";")
    reg = lm.LinearRegression()
    
    print(reg.fit(dataframe[['user', 'x', 'y']], dataframe['pace']))
    #reg.fit(dataframe[[ 'y','x', 'user']], dataframe['pace'])
    coef= reg.coef_
    print('coef')
    print(coef)
    intercept=reg.intercept_
    print('intercept:')
    print(intercept)
    predict= reg.predict([coef])
    print('Prediction:')
    print(predict)
    print('\r\n')
    list= [intercept, predict]
    saveData(list)

    

    





