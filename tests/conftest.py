import pytest
from src.decorators import *
from src.model import *
from src.savers import *
from src.utils import *
from src.vacancy import *

vac1_for_test = Vacancy(title="title1", desc="title1 desc", salary_from=50_000, salary_to=60_000, url="http://example.com")
vac2_for_test = Vacancy(title="title2", desc="title2 desc", salary_from=40_000, salary_to=180_000, url="http://example.org")
vac3_bad_test = Vacancy(title="ti3", desc="title3 desc", salary_from=None, salary_to=None, url="http://example.org")


@pytest.fixture
def get_one_test_vacancy():
    return vac1_for_test

@pytest.fixture
def get_one_bad_vacancy():
    return vac3_bad_test

@pytest.fixture
def get_vacancy_test_list():
    return [vac1_for_test, vac2_for_test]

FILE_FOR_EASY_TEST = "file_for_easy_test.json"
jssaver_test = JSONSaver(FILE_FOR_EASY_TEST, [vac1_for_test, vac2_for_test])
jssaver_bad = JSONSaver("file_for_bad_test.json", [vac1_for_test, vac2_for_test])

@pytest.fixture
def get_jssaver_test():
    return jssaver_test

@pytest.fixture
def get_jssaver_bad():
    return jssaver_bad

@pytest.fixture
def get_jssaver_filename():
    return FILE_FOR_EASY_TEST

@pytest.fixture
def get_utils_filename():
    return FILE_FOR_EASY_TEST