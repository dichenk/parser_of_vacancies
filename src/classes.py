import requests
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

    def __init__(self, nm):
        self.__vacancy = self.__get_request(nm)
        print(self.__vacancy.loc[1]['employer']['name'])

    
    def __len__(self):
        return len(self.__vacancy)

#    @property
#    def vacancy(self):
#        return self.__vacancy

    def __get_request(self, nm):
        if os.path.isfile('hh_vac.txt'):
            os.remove('hh_vac.txt')
        params = {
                'text': nm,
                'page': 1,
                'per_page': 100
                }
        response = pd.DataFrame()
        for i in range(1):
            params['page'] = i
            try:
                response_big = requests.get(self.__link, params).json()
            except:
                continue
            response_big = pd.DataFrame.from_dict(response_big)
            response_items = response_big.loc[:]['items']
            response_small = pd.DataFrame(list(response_items))
            response = pd.concat([response, response_small])
        response.to_csv('hh_vac.txt', sep=';', index=False)
        return response

class SuperJob(Engine):
    __link = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, nm):
        self.__vacancy = self.__get_request(nm)
        print(self.__vacancy.loc[1]['firm_name'])


    
    def __len__(self):
        return len(self.__vacancy)
    
#    @property
#    def vacancy(self):
#        return self.__vacancy
    
    def __get_request(self, nm):
        if os.path.isfile('sj_vac.txt'):
            os.remove('sj_vac.txt')
        params = {
                'keyword': nm,
                'page': 1,
                'count': 100
                }
        headers = {
                'Host': 'api.superjob.ru',
                'X-Api-App-Id': 'v3.r.137236372.6701c523f626cc54496d0761155a406797f44554.9e5dd41f3bccd577b32afe4ed3daf00c2ec08b63',
                'Authorization': 'Bearer r.000000010000001.example.access_token',
                'Content-Type': 'application/x-www-form-urlencoded'
                }
        response = pd.DataFrame()
        for i in range(1):
            params['page'] = i
            try:
                response_big = requests.get(self.__link, headers=headers, params=params).json()
            except:
                continue
            response_big = pd.DataFrame.from_dict(response_big)
            response_items = response_big.loc[:, 'objects']
            response_small = pd.DataFrame(list(response_items))
            response = pd.concat([response, response_small], axis=0)
        response.to_csv('sj_vac.txt', sep=';' )
        return response
        
class Vacancy:
    def __init__(self, vac_name = 'python'):
        self.__vac_key = vac_name
        self.__name = []
        self.__salary = []
        self.__place_of_work = []
        self.__experience = []
        self.__vac_hh = self.__take_from_hh(vac_name)
        self.printing()
        self.__vac_sj = self.__take_from_sj(vac_name)
        self.amount_of_vacancies = len(self.__vac_hh) + len(self.__vac_sj)
    
    def printing(self):
        for i in range(10):
            print('.', end='')
            time.sleep(1)
            if i == 5:
                print('да-да, я все еще ищу', end=' ')
        print()
    
    def find_me_offer(self, a, b, c):
        self.__vac_hh
        print(a, b, c)
        
    @staticmethod
    def __take_from_hh(nm):
        hh = HeadHunter(nm)
        return hh

    @staticmethod
    def __take_from_sj(nm):
        sj = SuperJob(nm)
        return sj
    
    def __repr__(self):
        #return f'name: {self.__name}\nlnk: {self.__link},\nabout: {self.__about},\nsalary: {self.__salary}'
        return str(len(self.__whatever) + len(self.__whatever2))

#    @property
#    def name(self, nm):
#        self.__name = nm
