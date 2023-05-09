""" utils for working with json-format file"""
import time
import json
import os
from pprint import pprint


def print_time_to_work(tell_me_about_you):
    """
    decorator with parameter
    :param tell_me_about_you: I guess to see where are we going from (main or module)
    :return: link to real_decorator func
    """

    def real_decorator(function):
        """
        I am real decorator, but I can use parameter from above decorator
        :param function: our function which we need to decorate
        :return: link to wrapper
        """

        # print("я вижу что ты пришел из", tell_me_about_you)
        def wrapper(*args):
            """ I  only decorator inside other decorator. I going to wrap your function"""
            print("I see you come from", tell_me_about_you)
            print("start reading file", *args)
            start_time = time.perf_counter()
            res = function(*args)  # it's our function with they arguments, and it must be returned
            end_time = time.perf_counter()
            print(f"Time taken for file open is {end_time - start_time}")
            return res

        return wrapper

    return real_decorator


def light_print_time_to_work(function):
    """
    I am light decorator
    :param function: our function which we need to decorate
    :return: link to wrapper
    """
    def wrapper(*args):
        """ I  just easy decorator. I going to wrap your function"""
        print(f"start function {function}", *args)
        start_time = time.perf_counter()
        res = function(*args)  # it's our function with they arguments, and it must be returned
        end_time = time.perf_counter()
        print(f"time taken for function {end_time - start_time}")
        return res

    return wrapper


#@print_time_to_work(__name__)
@light_print_time_to_work
def load_from_json_file(filename: str = './vacancy.json') -> dict:
    """ load any information from json-format file and return it"""

    # load from file
    if not os.path.exists(filename):
        return {}  # we did not find file and need to return nothing
        # seriously we need to create ecxeption
    with open(filename, 'r', encoding='utf-8') as fh:  # open file
        data = json.load(fh)  # load data
    return data


@light_print_time_to_work
def write_to_json_file(filename, *text):
    with open(filename, "w") as f:
        f.write(*text)





# this block for a self-test
if __name__ == '__main__':
    load_from_json_file("no_exist_file.json")
