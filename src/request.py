import requests
import json
import os

params = {
        'text': 'NAME:Python',
        'area': 1,
        'page': 1,
        'per_page': 100
        }

response = requests.get('https://api.hh.ru/vacancies', params).json()
f = open('hhanswer.txt', mode='w')
f.write(json.dumps(response, ensure_ascii=False))
f.close()

    

