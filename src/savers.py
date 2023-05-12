import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from config.config import *


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
    def write(self):
        list_for_write = []
        for vac in self.datalist:
            list_for_write.append(vac.get_json())
        data = json.dumps(list_for_write, indent=2, ensure_ascii=False)
        with open(self.filename, 'w', encoding=CODING_PAGE) as f:
            #json.dump(list_for_write, f, ensure_ascii=False)
            f.write(data)


    def read(self):
        """
        read file (self.filename)
        :return: list of Vacancy-class object wich was filled from file
        """
        if self.filename and os.path.isfile(self.filename):
            vacancylist = []
            with open(self.filename, 'r', encoding=CODING_PAGE) as f:
                data = json.load(f)
            print("data", data)
            if data is not None:
                for num, item in enumerate(data):
                    vacancy = Vacancy()
                    # print(num)
                    try:
                        vacancy.title = item["title"]
                        # vacancy.salary_min = item["salary"]["from"]
                        # vacancy.salary_max = item["salary"]["to"]
                        # vacancy.url = item["alternate_url"]
                        # vacancy.description = item["description"]
                        vacancylist.append(vacancy)
                    except Exception:
                        print("bad data in file")

        else:
            # raise(FileNotFoundException)
            print("File not found")
        return vacancylist

class CSVSaver(ABCSaver):
    ...


class BDSaver(ABCSaver):
    pass
