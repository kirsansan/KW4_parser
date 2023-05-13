from src.model import *
from src.savers import *


def read_big_apiHH():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    # m1.write_to_file(FILE_FOR_WRITE_RAW_DATA)
    vl = m1.get_parsed_data()
    saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    saver.write()


def read_big_apiSJ():
    m4 = Model_SuperJob({"text": "python", "area": 0})
    # m4.connect_to_API(0, 100)
    m4.get_big_data_step_by_step(files_write_flag=True)
    # m4.print_content()
    # m4.write_to_file(FILE_FOR_WRITE_RAW_DATA_SJ)
    # m1.get_big_data_step_by_step(files_write_flag=True)
    vl = m4.get_parsed_data()
    # print(len(vl))
    # [print(v) for v in vl]

    # saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    # saver.write()


def read_both_API():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    # m1.write_to_file(FILE_FOR_WRITE_RAW_DATA)
    m4 = Model_SuperJob({"text": "python", "area": 2})
    m4.get_big_data_step_by_step(files_write_flag=True)

    vl = m1.get_parsed_data()
    vl.extend(m4.get_parsed_data())

    saver = JSONSaver(FILE_FOR_VACANCY_JSON, vl)
    saver.write()


def print_big_apiHH():
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_big_data_step_by_step(files_write_flag=True)
    vl = m1.vacancy_list
    print(len(vl))
    [print(v) for v in vl]


def read_vacancy_data_file():
    saver = JSONSaver(FILE_FOR_VACANCY_JSON)
    vvl: list[Vacancy] = saver.read()
    # print(vvl)
    vvl.sort(reverse=True)
    print("================================================================")
    print(vvl)


def read_raw_fileHH():
    m2 = Model_HH({"text": "python"})
    m2.load_from_file(FILE_FOR_WRITE_RAW_DATA)
    # m2.print_content()
    m2.get_parsed_data()
    print(m2.vacancy_list)


def read_raw_fileSJ():
    m3 = Model_SuperJob({"text": "python"})
    m3.load_from_file(FILE_FOR_WRITE_RAW_DATA_SJ)
    # m2.print_content()
    m3.get_parsed_data()
    print(m3.vacancy_list)
    print(len(m3.vacancy_list))


if __name__ == '__main__':
    # read_big_apiHH()
    # read_raw_fileHH()
    # read_vacancy_data_file()

    # read_big_apiSJ()
    # read_raw_fileSJ()

    read_both_API()

    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # print(filter_words)

    # v1 = Vacancy("asas", "desc1", 1, None, "url")
    # v2 = Vacancy("bsbs", "desc2", None, None, "url")
    # print(v1 > v2)

    # m1.get_data_from_API()
    # # m1.print_content()

    # m1.write_to_file()
    # m1.load_from_file()
    # m1.print_content()
