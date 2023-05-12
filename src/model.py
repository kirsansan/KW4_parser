from abc import ABC, abstractmethod
import requests

import src.utils
from src.vacancy import Vacancy
from src.utils import *
from config.config import *

class Model(ABC):
    def __init__(self, params=None):
        self.params = params
        self.vacancy_list: list[:Vacancy] = []
        self.content = None
        self.content_for_print = None

    def set_params(self, params):
        """ Set params for searchin
        format is {"text": "text for searching", "area": "area code"}"""
        self.params = params


    def add_new_vacancy(self):
        vacancy = Vacancy()
        self.vacancy_list.append(vacancy)

    def write_to_file(self, filename=FILE_FOR_WRITE):
        if self.content is not None:
            src.utils.write_to_json_file(filename, self.content)

    def load_from_file(self, filename=FILE_FOR_WRITE):
        self.content = src.utils.load_from_json_file(filename)


    def print_content(self):
        content_for_print = json.dumps(self.content, indent=6, ensure_ascii=False)
        print(content_for_print)

    @abstractmethod
    def connect_to_API(self):
        pass

    @abstractmethod
    def get_data_from_API(self):
        pass

    @abstractmethod
    def get_parsed_data(self):
        pass


class Model_HH(Model):
    def __init__(self, params: dict = None):
        """

        :param params: {"text": "text for searching", "area": "area code"}
        """
        super().__init__(params)
        self.connector = None
        self.content = None


    def get_data_from_API(self):
        self.connect_to_API()
        return self.content

    def connect_to_API(self):
        """
        we need to create request shuch as 'https://api.hh.ru/vacancies?text=java&area=1'
        :return:
        """
        url = "https://api.hh.ru/vacancies"
        url += f"?text={self.params['text']}&area={self.params['area']}"
        headers = {"User-Agent": "K_ParserApp/1.0"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            #pprint(response.text)
            #self.content = json.dumps(response.text, indent=6, ensure_ascii=False)
            self.content = json.loads(response.text)
        print("HH API response is:", response)

    def get_parsed_data(self):
        vacancy_list: list[:Vacancy] = []
        for num, item in enumerate(self.content["items"]):
            vacancy = Vacancy()
            print(num)
            try:
                vacancy.title = item["name"]
                vacancy.salary_min = item["salary"]["from"]
                vacancy.salary_max = item["salary"]["to"]
                vacancy.url = item["alternate_url"]
                vacancy.description = item["description"]

            except Exception:
                print("bad data it item")
            vacancy_list.append(vacancy)
        return vacancy_list


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

    def get_parsed_data(self):
        ...


