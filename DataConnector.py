import pandas as pd
import glob

# create a Dataframe from all files
def createDataFrames():
    dframes = pd.DataFrame()
    for file in glob.iglob(r'.\Data\*.csv'):
        dataframe = pd.read_csv(file, sep=";")
        dframes = dframes.append(dataframe, ignore_index= True)
    return dframes






   
    




    