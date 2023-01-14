import requests
import json
import os
import pandas as pd
from abc import abstractmethod

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
        print(self.__vacancy)
        
    @property
    def vacancy(self):
        return self.__vacancy

    @classmethod
    def __get_request(cls):
        params = {
                'text': 'Python',
                'area': 1,
                'page': 1,
                'per_page': 100
                }
        responce_big = pd.DataFrame.from_dict(requests.get(cls.__link, params).json())
        responce_items = responce_big.loc[:]['items']
        responce_small = pd.DataFrame(list(responce_items))
        responce_small.to_csv('vac-vac.txt', sep='\t', index=False)

#        responce_vac = pd.DataFrame.from_dict(requests.get('https://api.hh.ru/vacancies/73141535').json())
        
        return len(responce_big)
 #       return responce_small.loc[1,['employer', 'name', 'alternate_url', 'snippet']]
 #       return responce_small.loc[1]

class SuperJob(Engine):
    __link = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.__vacancy = self.__get_request()
        print(self.__vacancy)
    
    @property
    def vacancy(self):
        return self.__vacancy
    
    @classmethod
    def __get_request(cls):
        params = {
                'keyword': 'python'
                }
        headers = {
                'Host': 'api.superjob.ru',
                'X-Api-App-Id': 'v3.r.137236372.6701c523f626cc54496d0761155a406797f44554.9e5dd41f3bccd577b32afe4ed3daf00c2ec08b63',
                'Authorization': 'Bearer r.000000010000001.example.access_token',
                'Content-Type': 'application/x-www-form-urlencoded'
                } 
        response = requests.get(cls.__link, headers=headers, params=params).json()
        return response
        
class Vacancy:
    def __init__(self, nm = None, lnk = None, abt = None, slr = None):
        self.__name = nm
        self.__link = lnk
        self.__about = abt
        self.__salary = slr
        self.__whatever = self.__take_from_sj()

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

    @property
    def name(self, nm):
        self.__name = nm
