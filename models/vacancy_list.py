from src.vacancy import Vacancy


class VacancyModel:

    def __init__(self):
        self.__all = []

    def sorting(self):
        ...

    def extend(self, new):
        if type(new) == type(list) and type(new[0]) == type(Vacancy):
            self._all = []
            self.__all.extend(new)

    @property
    def all(self):
        return self.__all

    @all.setter
    def all(self, value):
        self.extend(value)
