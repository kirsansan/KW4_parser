import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from config.config import *


class ABCSaver(ABC):
    def __init__(self, filename, datalist: list[:Vacancy]):
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
        with open(self.filename, 'w', encoding=CODING_PAGE) as f:
            for vac in self.datalist:
                json.dump(vac.get_json(), f, ensure_ascii=False)

    def read(self):
        pass


class CSVSaver(ABCSaver):
    ...


class BDSaver(ABCSaver):
    pass
