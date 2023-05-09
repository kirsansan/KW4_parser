from abc import ABC, abstractmethod

import src.utils
from src.vacancy import Vacancy
from src.utils import *
from config.config import *

class Model(ABC):
    def __init__(self, params=None):
        self.params = params
        self.vacancy_list: list[:Vacancy] = []
        self.content = None

    def add_new_vacancy(self):
        vacancy = Vacancy()
        self.vacancy_list.append(vacancy)

    def write_to_file(self, filename=FILE_FOR_WRITE):
        if self.content is not None:
            src.utils.write_to_json_file(filename, self.content)

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
        self.content = None

    def get_data_from_API(self):
        self.connect_to_API()
        return {"data": "HH.somedata"}

    def connect_to_API(self):
        ...

class Model_SuperJob(Model):
    def __init__(self, params=None):
        super().__init__(params)
        self.connector = None
        self.content = None

    def get_data_from_API(self):
        self.connect_to_API()
        self.content = {"data": "SuperJob.somedata"}
        return self.content

    def connect_to_API(self):
        ...


