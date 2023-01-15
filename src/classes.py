import requests
import json
import os
import pandas as pd
from abc import abstractmethod
import time

class Engine():
    @abstractmethod
    def get_request(self):
        return
    @staticmethod
    def get_connector(file_name):
        pass

class HeadHunter(Engine):
    __link = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.__vacancy = self.__get_request()
        print(len(self.__vacancy))
        
#    @property
#    def vacancy(self):
#        return self.__vacancy

    @classmethod
    def __get_request(cls):
        params = {
                'text': 'Python разработчик',
                'page': 1,
                'per_page': 100
                }
        response = pd.DataFrame()
        for i in range(6):
            params['page'] = i
            response_big = requests.get(cls.__link, params).json()
            response_big = pd.DataFrame.from_dict(response_big)
            response_items = response_big.loc[:]['items']
            response_small = pd.DataFrame(list(response_items))
            response = pd.concat([response, response_small])
        response.to_csv('hh_vac.txt', sep=';', index=False)
        return response

class SuperJob(Engine):
    __link = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.__vacancy = self.__get_request()
        print(self.__vacancy)
        print(len(self.__vacancy))
    
#    @property
#    def vacancy(self):
#        return self.__vacancy
    
    @classmethod
    def __get_request(cls):
        params = {
                'keyword': 'python',
                'page': 1,
                'count': 100
                #        'page': 2
                }
        headers = {
                'Host': 'api.superjob.ru',
                'X-Api-App-Id': 'v3.r.137236372.6701c523f626cc54496d0761155a406797f44554.9e5dd41f3bccd577b32afe4ed3daf00c2ec08b63',
                'Authorization': 'Bearer r.000000010000001.example.access_token',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
        response = pd.DataFrame()
        for i in range(0, 6):
            params['page'] = i
            response_big = requests.get(cls.__link, headers=headers, params=params).json()
            response_big = pd.DataFrame.from_dict(response_big)
            response_items = response_big.loc[:, 'objects']
            response_small = pd.DataFrame(list(response_items))
            response = pd.concat([response, response_small], axis=0)
        response.to_csv('sj_vac.txt', sep=';' )

        return response
        
class Vacancy:
    def __init__(self, nm = None, lnk = None, abt = None, slr = None):
        self.__name = nm
        self.__link = lnk
        self.__about = abt
        self.__salary = slr
        print('before')
        self.__whatever = self.__take_from_sj()
        print('first complited')
#        self.__whatever2 = self.__take_from_hh()
#        print('second complited')

    @staticmethod
    def __take_from_hh(what = None):
        hh = HeadHunter()
        return hh

    @staticmethod
    def __take_from_sj(what = None):
        sj = SuperJob()
        return sj
    
    def __repr__(self):
        return f'name: {self.__name}\nlnk: {self.__link},\nabout: {self.__about},\nsalary: {self.__salary}'

#    @property
#    def name(self, nm):
        self.__name = nm
