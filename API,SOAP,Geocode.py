#%%
import requests as rq
import json
data = rq.get('https://geocode-maps.yandex.ru/1.x?geocode=Самара&apikey=6137649b-ea10-4393-96a3-9bb0e570ea06&format=json&results=1')
data_set = json.loads(data.content)
print(data_set['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0])