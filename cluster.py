from pandas.core.frame import DataFrame
import pandas as pd
import glob
import matplotlib.pyplot  as plt
import numpy
import math
from sklearn.neighbors import KNeighborsClassifier


def createDataFrames():
    dframes = pd.DataFrame()
    
    for file in glob.iglob(r'C:\Users\thomi\OneDrive\Desktop\BigData-master\BigData\Data\*.csv'):
        print("hier...")
        dataframe = pd.read_csv(file, sep=";")
        dframes = dframes.append(dataframe, ignore_index= True)
    return dframes


def KNNgetUser(file):
    df = createDataFrames()
    print(df)
    dfx = df[['pace','x','y']]
    dfy = df['user']
    classifier =KNeighborsClassifier(n_neighbors = 5 )
    classifier.fit(dfx,dfy)
    y_pred= classifier.predict(pd.read_csv(file, sep=";"))
    return y_pred
    




    