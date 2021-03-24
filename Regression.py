#%%
import numpy as np
import matplotlib.pyplot as plot
import requests as rq
import openpyxl as oxl
import scipy.stats as st
import math as m
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression 
data = pd.read_csv('http://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
data['%'] = 100*data['UnemployedDisabled']/data['UnemployedTotal']
data_gr = data.groupby('Year').filter(lambda x: x['%'].count() > 5)
avg = data_gr.groupby('Year').mean()
x = np.array(avg.index).reshape(len(avg.index),1)
y = np.array(avg['%']).reshape(len(avg.index),1)
regress=LinearRegression()
regress.fit(x,y)
x = np.append(x, [2020]).reshape(len(avg.index)+1, 1)
print(regress.predict(np.array(2020).reshape(1,1)).round(2))