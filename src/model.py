from abc import ABC, abstractmethod
from src.vacancy import Vacancy

class Model(ABC):
    def __init__(self, params=None):
        self.params = params
        self.vacancy_list: list[:Vacancy] = []

    def add_new_vacancy(self):
        vacancy = Vacancy()
        self.vacancy_list.append(vacancy)


    @abstractmethod
    def connect_to_API(self):
        pass

    @abstractmethod
    def get_data_from_API(self):
        pass


class Model_HH(Model):
    def __init__(self, params=None):
        super().__init__(params)
        self.connector = None

    def get_data_from_API(self):
        self.connect_to_API()
        return {"data": "HH.somedata"}

    def connect_to_API(self):
        ...

class Model_SuperJob(Model):

    def get_data_from_API(self):
        self.connect_to_API()
        return {"data": "SuperJob.somedata"}

    def connect_to_API(self):
        ...