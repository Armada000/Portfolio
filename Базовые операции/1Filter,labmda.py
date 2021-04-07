#%%
import numpy as np
import matplotlib.pyplot as plot
import requests as rq
import openpyxl as oxl
import scipy.stats as st
import math as m
import pandas as pd
data= pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
data['%']= data.apply(lambda x: x[6]/x[7]*100, axis=1)
data=data[data['%']<2]
data=data.set_index('Year').sort_index()
print(data.index[0])