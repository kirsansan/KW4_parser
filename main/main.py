# from setuptools.config._validate_pyproject.formats import url

from src.model import *
from src.savers import *


def read_big_api():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    vl = m1.get_parsed_data()
    saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    saver.write()


def print_big_api():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    vl = m1.vacancy_list
    print(len(vl))
    [print(v) for v in vl]


def read_vacancy_data_file():
    saver = JSONSaver(FILE_FOR_VACANCY_JSON)
    vvl: list[Vacancy] = saver.read()
    print(vvl)
    #vvl.sort(reverse=True)
    print("================================================================")
    print(vvl)


def read_raw_file():
    m2 = Model_HH()
    m2.load_from_file(FILE_FOR_WRITE_RAW_DATA)
    # m2.print_content()
    m2.get_parsed_data()
    print(m2.vacancy_list)


if __name__ == '__main__':
    # read_big_api()
    # read_raw_file()
    read_vacancy_data_file()

    # m1.get_data_from_API()
    # # m1.print_content()

    # m1.write_to_file()
    # m1.load_from_file()
    # m1.print_content()
