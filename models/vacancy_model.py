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

    def filter_by_strings(self, keys, vacancies_for_search=None) -> list[Vacancy]:
        tmp_vacancy_list = []
        if not vacancies_for_search:
            vacancies_for_search = self.__all
        for item in vacancies_for_search:
            is_condition1 = set(keys) & set(item.title.split())
            is_condition2 = set(keys) & set(str(item.description).split())
            if is_condition2 or is_condition1:
                tmp_vacancy_list.append(item)
        return tmp_vacancy_list

    def filter_by_salary(self, salary_key: int, vacancies_for_search=None) -> list[Vacancy]:
        tmp_vacancy_list = []
        if not vacancies_for_search:
            vacancies_for_search = self.__all
        for item in vacancies_for_search:
            is_condition1 = item.salary_min > salary_key
            if is_condition1:
                tmp_vacancy_list.append(item)
        return tmp_vacancy_list