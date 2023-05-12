#from setuptools.config._validate_pyproject.formats import url

from src.model import *

if __name__ == '__main__':
    m1 = Model_HH({"text": "python", "area": 2})
    m1.get_data_from_API()
    # m1.print_content()

    m1.write_to_file()
    m1.load_from_file()
    m1.print_content()
