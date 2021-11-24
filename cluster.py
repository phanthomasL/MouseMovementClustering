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
        return "Ist es Thomas"
    elif (maxvalue == schwarki):
        return "Ist es Marvin"
    elif (maxvalue == taha):
        return "Ist es Taha"
    elif (maxvalue == bodemann):
        return "Ist es Philipp"




    




    