""" utils for working with json-format file"""

import json
import os
from config.config import CODING_PAGE
from pprint import pprint
from src.decorators import light_print_time_to_work, print_time_to_work



#@print_time_to_work(__name__)
@light_print_time_to_work
def load_from_json_file(filename: str = '../data/vacancy.json') -> dict:
    """ load any information from json-format file and return it"""
    # load from file
    if not os.path.exists(filename):
        raise FileNotFoundError(f"file %s not found or wrong path" % filename)
    with open(filename, 'r', encoding=CODING_PAGE) as fh:  # open file
        # data = fh.read()  # load data
        data = json.load(fh)
    return data


@light_print_time_to_work
def write_to_json_file(filename, text):
    """ just write data to json-format file"""
    data = json.dumps(text, indent=6, ensure_ascii=False)
    with open(filename, "w", encoding=CODING_PAGE) as f:
        # json.dump(data, f, ensure_ascii=False)
        f.write(data)


def sort_list_of_objects(objects: list):
    """Sort list of objects.
       Objects need to have ability to compare
       In the distance future I want to include lambda to sort them"""
    objects.sort(reverse=True)


def sample_list_of_objects(objects: list, lambda1):
    """Sort list of objects.
       Objects need to have ability to compare
       In the distance future I want to include lambda to sort them"""
    return [i for i in objects if lambda1(i)]


# this block for a self-test
if __name__ == '__main__':
    #load_from_json_file("no_exist_file.json")
    d = load_from_json_file("../tests/file_for_easy_test.json")
    print(d)

