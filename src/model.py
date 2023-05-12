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


    # def add_new_vacancy(self):
    #     vacancy = Vacancy()
    #     self.vacancy_list.append(vacancy)

    def write_to_file(self, filename=FILE_FOR_WRITE_RAW_DATA):
        if self.content is not None:
            src.utils.write_to_json_file(filename, self.content)

    def load_from_file(self, filename=FILE_FOR_WRITE_RAW_DATA):
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

    def connect_to_API(self, start_page=0, per_page=100):
        """
        we need to create request shuch as 'https://api.hh.ru/vacancies?text=java&area=1'
        :return:
        """
        url = "https://api.hh.ru/vacancies"
        url += f"?text={self.params['text']}&area={self.params['area']}"
        url += f"&page={start_page}&per_page={per_page}"
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
            # print(num)
            try:
                vacancy.title = item["name"]
                #print('item keys', item.keys())
                vacancy.url = item.get("alternate_url")

                if item.get("salary"):
                    vacancy.salary_min = item["salary"].get("from")
                    vacancy.salary_max = item["salary"].get("to")

                if item.get("description"):
                    print("item description is", item.get("description"))
                vacancy.description = item["snippet"].get("requirement")

            except Exception as err:
                print("bad data in item", err)
            vacancy_list.append(vacancy)
        self.vacancy_list.extend(vacancy_list)
        return vacancy_list


    def get_big_data_step_by_step(self):
        """
        fill self.vacancy_list with API
        no returns"""
        for i in range(0, 20):
            self.connect_to_API(i, 100)
            self.get_parsed_data()



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


