import pytest
from src.decorators import *
from src.model import *
from src.savers import *
from src.utils import *
from src.vacancy import *

vac1_for_test = Vacancy(title="title1", desc="title1 desc", salary_from=50_000, salary_to=60_000, url="http://example.com")
vac2_for_test = Vacancy(title="title2", desc="title2 desc", salary_from=40_000, salary_to=180_000, url="http://example.org")



@pytest.fixture
def get_one_test_vacancy():
    return vac1_for_test


@pytest.fixture
def get_vacancy_test_list():
    return [vac1_for_test, vac2_for_test]

