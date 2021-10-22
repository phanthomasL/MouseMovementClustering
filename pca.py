import numpy
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import glob
from matplotlib.pyplot import plot as plt

for file in glob.iglob(r'C:\Users\thomi\PycharmProjects\BigData\Data\*.csv'):
    dataframe = pd.read_csv(file, sep=";")
    dataframe.iloc()
    pca = PCA()
    sd = preprocessing.scale(dataframe.T)
    pca.fit(sd)
    pca_data = pca.transform(sd)
    #per_var = numpy.round(pca.explained_variance_ratio_*100)
    per_var = pca.explained_variance_ratio_
    print(per_var)
    plt