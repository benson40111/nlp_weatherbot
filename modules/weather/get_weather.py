import json
import requests

class Weather():
    def __init__(self, county, town):
        self.county = county
        self.town = town
    
    def askweather(self):
        with open('./city.json', 'r') as f:
            id = json.load(f)

        for x in id:
            if (self.town):
                for y in x['towns']:
                    if (self.town == y['name']):
                        id = y['id']
                        break
            else:
                if (self.county == x['name']):
                    id = x['id']
                    break
        return self.get_weather(id)
    
    def get_weather(self, id):
        text = requests.get('https://works.ioa.tw/weather/api/weathers/'+id+'.json').json()
        weather = text['desc']
        temp = str(text['temperature'])
        at = text['at']
        humidity = str(text['humidity'])
        rainfall = str(text['rainfall'])
        if (self.town):
            speech = self.town + '目前天氣為' + weather + ' 溫度為' + temp + '度' + '\n' + '更新時間:' + at + '\n' + '溼度為' + humidity + '%' + '\n' + '降雨機率為' + rainfall
            speech += ' 目前只能查詢當下天氣喔'
        else:
            speech = self.county + '目前天氣為' + weather + ' 溫度為' + temp + '度' + '\n' + '更新時間:' + at + '\n' + '溼度為' + humidity + '%' + '\n' + '降雨機率為' + rainfall
            speech += ' 目前只能查詢當下天氣喔'
        return speech

    def __str__(self):
        return self.askweather()

