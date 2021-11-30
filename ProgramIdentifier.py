from pandas.core.frame import DataFrame
import pandas as pd
import DataConnector
from sklearn.neighbors import KNeighborsClassifier

def KNNgetProgram(file):
    df = DataConnector.createDataFrames()
    print(df)
    dfx = df[['x','y','button']]
    dfy = df[['programm']]
    classifier = KNeighborsClassifier(n_neighbors = 5 )
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
        return "Es ist Chrome"