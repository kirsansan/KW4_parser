import os
import pytest
from src.savers import *
from src.vacancy import Vacancy


def test_saving_file(get_jssaver_test, get_jssaver_filename):
    if os.path.exists(get_jssaver_filename):
        os.remove(get_jssaver_filename)
    get_jssaver_test.write()
    assert os.path.exists(get_jssaver_filename)

def test_reading_file(get_jssaver_test, get_jssaver_filename):
    if not os.path.exists(get_jssaver_filename):
        get_jssaver_test.write()
    vl = get_jssaver_test.read()
    assert vl

def test_reading_non_exist_file():
    if not os.path.exists("non_exist_something.json"):
        tmp_saver = JSONSaver("non_exist_something.json", [])
    with pytest.raises(FileNotFoundError):
        tmp_saver.read()

def test_serialize_vacancy_to_json(get_jssaver_test, get_vacancy_test_list):
    assert get_jssaver_test.serialize_vacancy_to_json() == [{'description': 'title1 desc',
                                                              'salary_max': 60000,
                                                              'salary_min': 50000,
                                                              'title': 'title1',
                                                              'url': 'http://example.com'},
                                                             {'description': 'title2 desc',
                                                              'salary_max': 180000,
                                                              'salary_min': 40000,
                                                              'title': 'title2',
                                                              'url': 'http://example.org'}]

def test_deserialize_vacancy_to_json(get_jssaver_test, get_one_test_vacancy):
    vac: Vacancy = get_jssaver_test.deserialize_json_to_vacancy([{'description': 'title1 desc',
                                                              'salary_max': 60000,
                                                              'salary_min': 50000,
                                                              'title': 'title1',
                                                              'url': 'http://example.com'}])
    assert str(vac[0]) == str(get_one_test_vacancy)
