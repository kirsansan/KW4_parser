from abc import ABC, abstractmethod
from src.vacancy import Vacancy


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
    ...


class CSVSaver(ABCSaver):
    ...


class BDSaver(ABCSaver):
    pass
