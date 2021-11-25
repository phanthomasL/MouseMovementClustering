from pandas.core.frame import DataFrame
import pandas as pd
import glob
import matplotlib.pyplot  as plt

from sklearn.neighbors import KNeighborsClassifier


def createDataFrames():
    dframes = pd.DataFrame()
    
    for file in glob.iglob(r'.\Data\*.csv'):
        dataframe = pd.read_csv(file, sep=";")
        dframes = dframes.append(dataframe, ignore_index= True)
    return dframes


def KNNgetUser(file):
    df = createDataFrames()
    print(df)
    dfx = df[['pace']]
    dfy = df[['user']]
    classifier =KNeighborsClassifier(n_neighbors = 5 )
    classifier.fit(dfx,dfy)
    frame = pd.read_csv(file, sep=";")
    print(frame)
    frame = frame[['pace']]
    print(frame)
    y_pred= classifier.predict(frame)
    thomas = (y_pred == 1).sum()
    schwarki = (y_pred == 2).sum()
    taha = (y_pred == 3).sum()
    bodemann = (y_pred == 4).sum()
    maxvalue = max([thomas, schwarki, taha, bodemann])

    if (maxvalue == thomas):
        return "Es ist Thomas"
    elif (maxvalue == schwarki):
        return "Es ist Marvin"
    elif (maxvalue == taha):
        return "Es ist Taha"
    elif (maxvalue == bodemann):
        return "Es ist Philipp"


def KNNgetProgram(file):
    df = createDataFrames()
    print(df)
    dfx = df[['x','y','button']]
    dfy = df[['programm']]
    classifier =KNeighborsClassifier(n_neighbors = 5 )
    classifier.fit(dfx,dfy)
    frame = pd.read_csv(file, sep=";")
    print(frame)
    frame = frame[['x','y','button']]
    print(frame)
    y_pred= classifier.predict(frame)
    excel = (y_pred == 1).sum()
    vsc = (y_pred == 2).sum()
    webex = (y_pred == 3).sum()
    
    maxvalue = max([excel, vsc, webex])

    if (maxvalue == excel):
        return "Es ist Excel"
    elif (maxvalue == vsc):
        return "Es ist Visual studio code"
    elif (maxvalue == webex):
        return "Es ist WebEx"
   
    




    