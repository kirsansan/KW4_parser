import pytest
import os

import src.utils


def test_load_file(get_utils_filename):
    if not os.path.exists(get_utils_filename):
        raise FileNotFoundError
    some_json = src.utils.load_from_json_file(get_utils_filename)
    assert some_json == [{'description': 'title1 desc',
                          'salary_max': 60000,
                          'salary_min': 50000,
                          'title': 'title1',
                          'url': 'http://example.com'},
                         {'description': 'title2 desc',
                          'salary_max': 180000,
                          'salary_min': 40000,
                          'title': 'title2',
                          'url': 'http://example.org'}]


def test_write_to_json_file(get_utils_filename):
    if os.path.exists(get_utils_filename):
        os.remove(get_utils_filename)
    some_json = [{'description': 'title1 desc',
                  'salary_max': 60000,
                  'salary_min': 50000,
                  'title': 'title1',
                  'url': 'http://example.com'},
                 {'description': 'title2 desc',
                  'salary_max': 180000,
                  'salary_min': 40000,
                  'title': 'title2',
                  'url': 'http://example.org'}]
    src.utils.write_to_json_file(get_utils_filename, some_json)
    assert os.path.exists(get_utils_filename)


def test_load_non_exist_file():
    with pytest.raises(FileNotFoundError):
        src.utils.load_from_json_file("non_exist_something.json")
