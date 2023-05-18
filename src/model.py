from abc import ABC, abstractmethod
import requests

import src.utils
from src.vacancy import Vacancy
from src.utils import *
from config.config import *


class Model(ABC):
    """ Abstract class for model.
    model will be able to read data from API, parse it, read and write data from/to raw-files"""
    def __init__(self, params=None):
        self.params = params
        self.vacancy_list: list[:Vacancy] = []
        self.content = None
        self.content_inside: list = []

    def set_params(self, params):
        """ Set params for searchin
        format is {"text": "text for searching", "area": "area code"}"""
        self.params = params

    def write_to_file(self, filename=FILE_FOR_WRITE_RAW_DATA):
        """ Write to JSON-file in my own structure"""
        if self.content_inside is not None:
            src.utils.write_to_json_file(filename, self.content_inside)

    def load_from_file(self, filename=FILE_FOR_WRITE_RAW_DATA):
        """ Just read JSON-file in my own structure"""
        self.content_inside = src.utils.load_from_json_file(filename)

    def print_content(self):
        """ print data in human-friendly format if you want"""
        content_for_print = json.dumps(self.content_inside, indent=6, ensure_ascii=False)
        print(content_for_print)

    @abstractmethod
    def connect_to_API(self):
        """ One step connect to API"""
        pass

    @abstractmethod
    def get_parsed_data(self):
        """ parse data which received from API or raw-file"""
        pass

    @abstractmethod
    def get_data_from_API(self):
        """ one-step receive data from API for creating example files"""
        pass


class Model_HH(Model):

    def get_data_from_API(self):
        self.connect_to_API()
        return self.content

    def connect_to_API(self, start_page=0, per_page=100):
        """
        we need to create request such as 'https://api.hh.ru/vacancies?text=java&area=1'
        :return:
        """
        url = MAIN_REQUEST_FOR_HH
        url += f"?enable_snippets=true&text={self.params['text']}&area={self.params['area']}"
        url_with_pages = url + f"&page={start_page}&per_page={per_page}"
        print(url_with_pages)  # need chane to logger
        headers = {"User-Agent": MY_APP_NAME}
        response = requests.get(url_with_pages, headers=headers)
        if response.status_code == 200:
            self.content = json.loads(response.text)
            self.content_inside.extend(self.content.get("items"))
        print("HH API response is:", response)  # need chane to logger

    def get_parsed_data(self):
        """ parse data which received from API or raw-file for HedHunter format"""
        for item in self.content_inside:
            vacancy = Vacancy()
            try:
                vacancy.title = item["name"]
                vacancy.url = item.get("alternate_url")
                if item.get("salary"):
                    vacancy.salary_min = item["salary"].get("from") if item["salary"].get("from") else 0
                    vacancy.salary_max = item["salary"].get("to") if item["salary"].get("to") else 0
                vacancy.description = item["snippet"].get("requirement")
            except Exception as err:
                print("bad data in item", err)
            self.vacancy_list.append(vacancy)
        return self.vacancy_list

    @light_print_time_to_work
    def get_big_data_step_by_step(self, files_write_flag=False):
        """
        fill self.vacancy_list with API
        no returns"""
        steps = 0
        self.connect_to_API(19, 100)  # we need to know how many steps will be, so - see in tail
        if self.content["items"] == []:
            steps = self.content.get("pages")
        for i in range(0, steps):
            self.connect_to_API(i, 100)
        self.get_parsed_data()
        if files_write_flag:
            self.write_to_file(FILE_FOR_WRITE_RAW_DATA)


class Model_SuperJob(Model):

    def get_data_from_API(self):
        self.connect_to_API()
        return self.content

    def connect_to_API(self, start_page=5, count=100):
        """
        we need to create request such as 'https://api.superjob.ru/2.0/vacancies/?t=4&count=100'
        :return:
        """
        url = MAIN_REQUEST_FOR_SJ
        url += f"/?&keyword={self.params['text']}&t={self.params['area']}"
        url_with_pages = url + f"&page={start_page}&count={count}"
        print(url_with_pages)    # need chane to logger
        headers = {"X-Api-App-Id": SUPER_JOB_KEY}
        response = requests.get(url_with_pages, headers=headers)
        if response.status_code == 200:
            self.content = json.loads(response.text)
            self.content_inside.extend(self.content.get("objects"))
        print("SurerJob API response is:", response)  # need chane to logger

    def get_parsed_data(self):
        """ parse data which received from API or raw-file for SuperJob format"""
        for item in self.content_inside:
            vacancy = Vacancy()
            try:
                vacancy.title = item["profession"]
                vacancy.url = item.get("link")
                vacancy.salary_min = item["payment_from"] if item["payment_from"] else 0
                vacancy.salary_max = item["payment_to"] if item["payment_to"] else 0
                vacancy.description = item["candidat"]
            except Exception as err:
                print("bad data in item", err)
            self.vacancy_list.append(vacancy)
        return self.vacancy_list

    @light_print_time_to_work
    def get_big_data_step_by_step(self, files_write_flag=False):
        """
        fill self.vacancy_list with API
        no returns"""
        steps = 0
        self.connect_to_API(0, 100)  # we need to know how many steps will be
        if self.content["objects"] != []:
            # print(self.content)
            total: int = self.content.get("total")
            steps = (total // 100)
        for i in range(1, steps):
            self.connect_to_API(i, 100)
        self.get_parsed_data()
        if files_write_flag:
            self.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
