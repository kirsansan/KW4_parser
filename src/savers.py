import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from config.config import *
from src.decorators import light_print_time_to_work, print_time_to_work


class ABCSaver(ABC):
    def __init__(self, filename, datalist: list[:Vacancy]=None):
        self.filename = filename
        self.datalist = datalist

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class JSONSaver(ABCSaver):

    @light_print_time_to_work
    def serialize_vacancy_to_json(self):
        list_for_write = []
        for vac in self.datalist:
            list_for_write.append(vac.get_json())
        return list_for_write

    @light_print_time_to_work
    def write(self):
        list_for_write = self.serialize_vacancy_to_json()
        data = json.dumps(list_for_write, indent=2, ensure_ascii=False)
        with open(self.filename, 'w', encoding=CODING_PAGE) as f:
            #json.dump(list_for_write, f, ensure_ascii=False)
            f.write(data)

    def deserialize_json_to_vacancy(self, data):
        vacancylist = []
        if data is not None:
            for num, item in enumerate(data):
                vacancy = Vacancy()
                try:
                    vacancy.title = item["title"]
                    vacancy.salary_min = item["salary_min"]
                    vacancy.salary_max = item["salary_max"]
                    vacancy.url = item["url"]
                    vacancy.description = item["description"]
                    vacancylist.append(vacancy)
                except Exception:
                    print("bad data in file")
                    continue
        return vacancylist

    def read(self):
        """
        read file (self.filename)
        :return: list of Vacancy-class object which was filled from file
        """
        if self.filename and os.path.isfile(self.filename):
            with open(self.filename, 'r', encoding=CODING_PAGE) as f:
                data = json.load(f)
            print("data", data)
        else:
            # raise(FileNotFoundException)
            print("File not found")
        return self.deserialize_json_to_vacancy(data)

class CSVSaver(ABCSaver):
    ...


class BDSaver(ABCSaver):
    pass
