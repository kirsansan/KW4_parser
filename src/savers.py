import json
from abc import ABC, abstractmethod

import src.utils
from src.vacancy import Vacancy
from config.config import *
from src.decorators import light_print_time_to_work, print_time_to_work


class ABCSaver(ABC):
    def __init__(self, filename, datalist: list[:Vacancy] = None):
        self.filename = filename
        self.datalist = datalist

    def set_datalist(self, datalist: list[:Vacancy]):
        """set data as list of Vacancy objects for saving"""
        self.datalist = datalist

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class JSONSaver(ABCSaver):

    def read(self):
        """
        read file (self.filename)
        :return: list of Vacancy-class objects which were filled from file
        """
        data = src.utils.load_from_json_file(self.filename)
        return self.deserialize_json_to_vacancy(data)

    def write(self):
        """
        write file (self.filename)
        :return: none
        """
        list_for_write = self.serialize_vacancy_to_json()
        src.utils.write_to_json_file(self.filename, list_for_write)

    @light_print_time_to_work
    def serialize_vacancy_to_json(self):
        """return all vacancies data in json format for writing"""
        list_for_write = []
        for vac in self.datalist:
            list_for_write.append(vac.get_json())
        return list_for_write

    def deserialize_json_to_vacancy(self, data) -> list[Vacancy]:
        """
        fill list of Vacancy objects from json-data format
        :param data: json-data
        :return: list of Vacancy-class objects
        """
        vacancy_list = []
        if data is not None:
            for item in data:
                vacancy = Vacancy()
                try:
                    vacancy.title = item["title"]
                    vacancy.salary_min = item["salary_min"] if item["salary_min"] else 0
                    vacancy.salary_max = item["salary_max"] if item["salary_max"] else 0
                    vacancy.url = item["url"]
                    vacancy.description = item["description"]
                    vacancy_list.append(vacancy)
                except Exception:
                    print("bad data in file")
                    continue
        return vacancy_list


class CSVSaver(ABCSaver):
    ...


class BDSaver(ABCSaver):
    pass
