#from setuptools.config._validate_pyproject.formats import url

from src.model import *
from src.savers import *

if __name__ == '__main__':
    m1 = Model_HH({"text": "python", "area": 2})
    # m1.get_data_from_API()
    # # m1.print_content()
    m1.get_big_data_step_by_step()
    m1.write_to_file()
    # m1.load_from_file()
    # m1.print_content()
    #vl = m1.get_parsed_data()
    vl = m1.vacancy_list
    print(len(vl))
    [print(v) for v in vl]


    saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    saver.write()

    # saver = JSONSaver(FILE_FOR_VACANCY_JSON)
    # vvl = saver.read()
    # print(vvl)
