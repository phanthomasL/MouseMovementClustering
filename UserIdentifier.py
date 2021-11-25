from pandas.core.frame import DataFrame
import pandas as pd
import DataConnector
from sklearn.neighbors import KNeighborsClassifier


def KNNgetUser(file):
    df = DataConnector.createDataFrames()
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