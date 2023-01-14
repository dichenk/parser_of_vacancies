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

class HH(Engine):
    __link = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.__vacancy = self.__get_request()
        print(self.vacancy)
        
    @property
    def vacancy(self):
        return self.__vacancy

    @classmethod
    def __get_request(cls):
        params = {
                'text': 'NAME:Python',
                'area': 1,
                'page': 1,
                'per_page': 100
                }
        responce = requests.get(cls.__link, params).json()
        f = open('hhanswer.txt', mode='w')
        f.write(json.dumps(responce, ensure_ascii=False))
        f.close()
        return responce

class Superjob(Engine):
    def get_request(self):
        pass

class Vacancy:
    def __init__(self, nm = None, lnk = None, abt = None, slr = None):
        self.__name = nm
        self.__link = lnk
        self.__about = abt
        self.__salary = slr
        self.__whatever =self.__take_from_hh()

    @staticmethod
    def __take_from_hh(what = None):
        hh = HH()
        return hh
    
    def __repr__(self):
        return f'name: {self.__name}\nlnk: {self.__link},\nabout: {self.__about},\nsalary: {self.__salary}'

    @property
    def name(self, nm):
        self.__name = nm
