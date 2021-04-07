#%%
import numpy as np
import matplotlib.pyplot as plot
import requests as rq
import openpyxl as oxl
import scipy.stats as st
import math as m
import pandas as pd
from bs4 import BeautifulSoup
req= rq.get('https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019')
html= BeautifulSoup(req.content)
table=html.find('table', {'id':'marketDataList'})
data=[]
for tr in table.find_all('tr'):
    tr =[td.get_text(strip=True) for td in tr.find_all('td')]
    if len(tr) > 0:
        data.append(tr)
data = pd.DataFrame(data, columns = ['ticker', 'time', 'price', '+-', '%', 'last c', 'o', 'min', 'max', 'sav', 'volume size', 'volume cost', 'market std'])
data=data[data['price']!='N/A']
data['%']=data['%'].str.replace('−','-').str.replace('%','').astype(float)
data= data.set_index('%').sort_index(ascending=False)
print(data['ticker'].head(1))