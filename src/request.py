from types import new_class
import requests
import json
import os
import classes


new_elem = classes.Vacancy()
print(new_elem)

'''
params2 = {
        'count': 2,
        'keywords': [
            {
                'keys': 'python'
            },
            {
                'skwc': 'particular',
                'keys': 'разработчик'
                }
            ],
        'period': 0
        }

params3 = {
        'keyword': 'Влад'
        }
response = requests.get('https://api.superjob.ru/2.0/vacancies/',
    headers={
        'Host': 'api.superjob.ru',
        'X-Api-App-Id': 'v3.r.137236372.6701c523f626cc54496d0761155a406797f44554.9e5dd41f3bccd577b32afe4ed3daf00c2ec08b63',
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application/x-www-form-urlencoded'
    }, 
params=params2).json()
with open('sjanswer.json', mode='w') as outfile:
    json.dump(response, outfile, ensure_ascii=False)

with open('sjanswer.json', mode='r') as outfile:
    for index, item in  enumerate(outfile):
        if index == 0:
            something = json.loads(item)
            print(something['objects'][0]['id'])
            print(len(something['objects']))

'''

    

