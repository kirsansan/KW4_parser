from setuptools.config._validate_pyproject.formats import url

from src.model import *

if __name__ == '__main__':
    m1 = Model_HH()
    print(m1.get_data_from_API()['data'])
    m2 = Model_SuperJob()
    print(m2.get_data_from_API()['data'])

    m1.add_new_vacancy()
    m1.add_new_vacancy()
    print(m1.vacancy_list)

    v1 = Vacancy("pioneer", salary=10_000, url="http://vk.ru")
    print(v1)
    v2 = Vacancy("student", salary=20_000, url="http://ubuntu.org")
    print(v2)
    print(v2 > v1)
