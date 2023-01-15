import requests
import os
import pandas as pd
from abc import abstractmethod

class Engine():
    
    @abstractmethod
    def get_request(self):
        return
    
    @abstractmethod
    def take_info_in_pandas(self):
        return

class HeadHunter(Engine):
    __link = 'https://api.hh.ru/vacancies'

    def __init__(self, nm):
        self.__vacancy = self.__get_request(nm)
        print(self.__vacancy.loc[1]['employer']['name'])
    
    def __len__(self):
        return len(self.__vacancy)

    def __get_request(self, nm):
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
        response.to_csv('vac_hh_' + nm + '.txt', sep=';', index=False)
        return response

    def take_info_in_pandas(self):
        return self.__vacancy

class SuperJob(Engine):
    __link = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, nm):
        self.__vacancy = self.__get_request(nm)
        print(self.__vacancy.loc[1]['firm_name'])

    def __len__(self):
        return len(self.__vacancy)
    
    def __get_request(self, nm):
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
        response.to_csv('vac_sj_' + nm + '.txt', sep=';' )
        return response

    def take_info_in_pandas(self):
        return self.__vacancy
        
class Vacancy:
    def __init__(self, vac_name = 'python'):
        self.__vac_hh = HeadHunter(vac_name)
        self.__vac_sj = SuperJob(vac_name)
        self.amount_of_vacancies = len(self.__vac_hh) + len(self.__vac_sj) 
    
    def find_the_offer(self):
        hh_vac = self.__vac_hh.take_info_in_pandas()
        hh_vac = hh_vac.loc[:, ['name', 'salary', 'alternate_url', 'employer', 'schedule']]
        
        hh_vac_sal = pd.json_normalize(hh_vac['salary'])
        hh_vac_sal.rename(columns = {'from':'payment_from', 'to':'payment_to'}, inplace=True)
        hh_vac_sal = hh_vac_sal.loc[:, ['payment_from', 'payment_to']]
        
        hh_vac_emp = pd.json_normalize(hh_vac['employer'])
        hh_vac_emp.rename(columns = {'name':'firm_name'}, inplace=True)
        hh_vac_emp = hh_vac_emp.loc[:, 'firm_name']

        hh_vac_sched = pd.json_normalize(hh_vac['schedule'])
        hh_vac_sched.rename(columns = {'name':'place_of_work'}, inplace=True)
        hh_vac_sched = hh_vac_sched.loc[:, 'place_of_work']
    
        hh_vac = hh_vac.loc[:, ['name', 'alternate_url']]
        hh_vac = pd.concat([hh_vac, hh_vac_sched, hh_vac_sal, hh_vac_emp], axis=1)
#        print(hh_vac.loc[hh_vac['place_of_work'] == 'Удаленная работа'])

        sj_vac = self.__vac_sj.take_info_in_pandas()
        print(sj_vac.columns)



    def __repr__(self):
        return str('kokoko')
