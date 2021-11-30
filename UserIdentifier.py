from pandas.core.frame import DataFrame
import pandas as pd
import DataConnector
from sklearn.neighbors import KNeighborsClassifier


def KNNgetUser(file):
    df = DataConnector.createDataFrames()
    print(df)
    dfx = df[['pace','timeInMsSinceStart','x', 'y']]
    dfy = df[['user']]
    classifier =KNeighborsClassifier(n_neighbors = 4 )
    classifier.fit(dfx,dfy)
    frame = pd.read_csv(file, sep=";")
    print(frame)
    frame = frame[['pace','timeInMsSinceStart','x','y']]
    print(frame)
    y_pred= classifier.predict(frame)
    thomas = (y_pred == 1).sum()
    print(thomas)
    schwarki = (y_pred == 2).sum()
    print(schwarki)
    taha = (y_pred == 3).sum()
    print(taha)
    bodemann = (y_pred == 4).sum()
    print(bodemann)
    maxvalue = max([thomas, schwarki, taha, bodemann])

    if (maxvalue == thomas):
        return "Es ist Thomas"
    elif (maxvalue == schwarki):
        return "Es ist Marvin"
    elif (maxvalue == taha):
        return "Es ist Taha"
    elif (maxvalue == bodemann):
        return "Es ist Philipp"