from src.vacancy import Vacancy


class VacancyModel:

    def __init__(self):
        self.__all: list[Vacancy] = []

    def sorting(self):
        """ method for feature. currently under construct"""
        ...

    def replace(self, new):
        """ update all information
        call this method before write new data"""
        if new:
            if type(new) == list and type(new[0]) == Vacancy:
                self.__all = []
                self.__all.extend(new)
        else:
            self.__all = []

    def extend(self, new):
        """Extend old data with new
         also using before writing"""
        if type(new) == list and type(new[0]) == Vacancy:
            self.__all.extend(new)

    @property
    def all(self):
        return self.__all

    @all.setter
    def all(self, value):
        self.replace(value)

    def filter_by_strings(self, keys, vacancies_for_search=None) -> list[Vacancy]:
        """ Filter all data by strings 'keys'
        only elements which insert string with words from 'keys'' will be able to safe
        ::param:: keys is a list(tuples) of strings
        ::return:: new list of Vacancy-calss objects (therefore reduce data)"""
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
        """ Filter all data by salary_min
        only elements which insert salary_min more than 'salary_key' will be able to safe
        ::param:: salary_key as integer
        ::return:: new list of Vacancy-calss objects (therefore reduce data)"""
        tmp_vacancy_list = []
        if not vacancies_for_search:
            vacancies_for_search = self.__all
        for item in vacancies_for_search:
            is_condition1 = item.salary_min > salary_key
            if is_condition1:
                tmp_vacancy_list.append(item)
        return tmp_vacancy_list