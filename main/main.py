from src.model import *

if __name__ == '__main__':
    m1 = Model_HH()
    print(m1.get_data_from_API()['data'])
    m2 = Model_SuperJob()
    print(m2.get_data_from_API()['data'])

    m1.add_new_vacancy()
    m1.add_new_vacancy()
    print(m1.vacancy_list)

    v1 = Vacancy()
    print(v1)
