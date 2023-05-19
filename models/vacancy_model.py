from src.vacancy import Vacancy


class VacancyModel:

    def __init__(self):
        self.__all: list[Vacancy] = []

    def sorting(self):
        ...

    def replace(self, new):
        if type(new) == list and type(new[0]) == Vacancy:
            self.__all = []
            self.__all.extend(new)

    def extend(self, new):
        if type(new) == list and type(new[0]) == Vacancy:
            self.__all.extend(new)

    @property
    def all(self):
        return self.__all

    @all.setter
    def all(self, value):
        self.replace(value)
