from pandas.core.frame import DataFrame
import numpy
import pandas as pd
from sklearn import preprocessing
import glob
import matplotlib.pyplot  as plt
import numpy
import math
from sklearn.neighbors import KNeighborsClassifier


def createDataFrames():
    dframes :  DataFrame 
    for file in glob.iglob(r'C:\Users\thomi\PycharmProjects\BigData\Data\*.csv'):
        dataframe = pd.read_csv(file, sep=";")
        dframes.append(dataframe)
    return dframes


def KNNgetUser(file):
    df = createDataFrames
    dfx = df['pace','x','y']
    dfy = df['user']
    classifier =KNeighborsClassifier(n_neighbors =5 )
    n_neighbors = classifier.fit(dfx,dfy)
    y_pred= classifier.predict(file)
    




    