import requests
from flask import jsonify
from modules.weather.get_weather import Weather
from modules.calc.calc import Calc
from urllib.parse import quote

# Using dialogflow api
with open('api_key', 'r') as f:
    api_key = f.read()

class Webhook():
    def __init__(self):
        self.req = None
        self.speech = ''
        self.speech_json = None
        self.__key = api_key

    def get_message(self, req):
        try:
            self.req = req.json()
            result = self.req.get('result')
            intentName = result.get('metadata').get('intentName')
            parameters = result.get('parameters')
            if (intentName == 'askweather'):
                county = parameters.get('weatherlocation')
                town = parameters.get('weatherTown')
                date = parameters.get('date')
                self.speech = str(Weather(county, town, date))
            elif (intentName == 'askcourse'):
                department = parameters.get('coursedepartement')
                category = parameters.get('coursecategory')
                grade = parameters.get('coursegrade')
                week = parameters.get('courseweek')
                time = parameters.get('coursetime')
                self.speech = 'localhost:8080/'
                if department:
                    self.speech += 'department=' + department + '&'
                if category:
                    self.speech += 'category=' + category + '&'
                if grade:
                    self.speech += 'grade=' + grade + '&'
                if week:
                    self.speech += 'week=' + week + '&'
                if time:
                    self.speech += 'time='
                    for i, x in enumerate(time):
                        if (i != len(time) - 1):
                            self.speech += x + ','
                        else:
                            self.speech += x
                    self.speech += '&'

            elif (intentName == 'askcalc'):
                querry = result.get('resolvedQuery')
                self.speech = Calc(querry).process()

            else:
                querry = result.get('resolvedQuery')
                querry = quote(querry)
                self.speech = 'https://www.google.com/search?q=' + querry
        except Exception as err:
            print(err)
            querry = result.get('resolvedQuery')
            querry = quote(querry)
            self.speech = 'https://www.google.com/search?q=' + querry
        return self.speech
    def return_json(self):
        self.speech_json = {'speech':self.get_message(req), 'source':'agent'}
        return jsonify(self.speech_json)
    def send_message(self, message):
        data = {
                'lang': 'zh-TW',
                'query': message,
                'sessionId': '123',
                'timezone': 'Asia/Hong_Kong'
               }

        header = {'Authorization':self.__key, 'content-type':'application/json;charset=UTF-8'}
        req = requests.post('https://api.dialogflow.com/v1/query?v=20150910', json=data, headers=header)
        text = self.get_message(req)
        if (text):
            return text
        else:
            return '對不起 我沒收到訊息 請再說一次'
