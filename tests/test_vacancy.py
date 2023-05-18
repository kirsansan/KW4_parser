

def test_prints(get_one_test_vacancy):
    assert str(get_one_test_vacancy) == 'title1 with salary from 50000 to 60000'
    assert str(get_one_test_vacancy) == 'title1 with salary from 50000 to 60000'
    assert repr(get_one_test_vacancy) == "Vacancy('title1', 50000-60000, http://example.com)"

def test_comparissions(get_vacancy_test_list):
    assert get_vacancy_test_list[0] >= get_vacancy_test_list[1]
    assert get_vacancy_test_list[0] > get_vacancy_test_list[1]
    assert get_vacancy_test_list[1] < get_vacancy_test_list[0]
    assert get_vacancy_test_list[1] <= get_vacancy_test_list[0]
    assert not (get_vacancy_test_list[0] == get_vacancy_test_list[1])
    assert (get_vacancy_test_list[0] != get_vacancy_test_list[1])

def test_get_json_format(get_one_test_vacancy):
    assert get_one_test_vacancy.get_json() == {'description': 'title1 desc',
                                                 'salary_max': 60000,
                                                 'salary_min': 50000,
                                                 'title': 'title1',
                                                 'url': 'http://example.com'}

def test_fill_empty(get_one_bad_vacancy):
    get_one_bad_vacancy.check_empty_salary()
    assert get_one_bad_vacancy.salary_min != None
    assert get_one_bad_vacancy.salary_max != None
    assert get_one_bad_vacancy.salary_max == 0
