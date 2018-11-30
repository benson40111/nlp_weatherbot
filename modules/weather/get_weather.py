import json
import requests
from datetime import date

class Weather():
    def __init__(self, county, town, date):
        self.county = county
        self.town = town
        self.date = date
    def askweather(self):
        d = date.today().isoformat()
        if (d != self.date and self.date):
            return '對不起 目前不能查其他時間喔'
        else:
            with open('./city.json', 'r') as f:
                city_id = json.load(f)

            for x in city_id:
                if (self.town):
                    for y in x['towns']:
                        if (self.town == y['name']):
                            city_id = y['id']
                            break
                else:
                    if (self.county == x['name']):
                        city_id = x['id']
                        break
            return self.get_weather(city_id)
    def get_weather(self, city_id):
        text = requests.get('https://works.ioa.tw/weather/api/weathers/'+city_id+'.json').json()
        weather = text['desc']
        temp = str(text['temperature'])
        at = text['at']
        humidity = str(text['humidity'])
        rainfall = str(text['rainfall'])
        if (self.town):
            speech = self.town + '目前天氣為' + weather + ' 溫度為' + temp + '度' + '\n' + '更新時間:' + at + '\n' + '溼度為' + humidity + '%' + '\n' + '降雨機率為' + rainfall
        else:
            speech = self.county + '目前天氣為' + weather + ' 溫度為' + temp + '度' + '\n' + '更新時間:' + at + '\n' + '溼度為' + humidity + '%' + '\n' + '降雨機率為' + rainfall
        speech += ' 目前只能查詢當下天氣喔'
        return speech

    def __str__(self):
        return self.askweather()

