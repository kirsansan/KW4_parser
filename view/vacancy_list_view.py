from config.config import MAX_COUNT_VACANCY_FOR_USER_DISPLAY
from src.vacancy import Vacancy


class VacancyListView:
    """ list of Vacancy-objects as data model"""

    def __init__(self):
        self.__max_count_object_print = MAX_COUNT_VACANCY_FOR_USER_DISPLAY
        self.filter_keyword = None
        self.filter_by_salary = None

    @property
    def max_lines_print(self):
        return self.__max_count_object_print

    @max_lines_print.setter
    def max_lines_print(self, num: int):
        if type(num) == int and num > 0:
            self.__max_count_object_print = num

    def print_all(self, data):
        """Print all what I know about vacancies"""
        if data:
            for i in data:
                print(i)
        else:
            print("vacancy list is empty yet")

    def print_ext_mode(self, data: list[Vacancy]):
        """beauty printing information"""
        counter = 0
        print("===============start of report=================")
        if data:
            for item in data:
                if counter > self.__max_count_object_print:
                    break
                print("Title      :", item.title)
                print("Description:", item.description)
                print("Salary from:", item.salary_min)
                print("Salary to  :", item.salary_min)
                print("url        :", item.url)
                print("")
                counter += 1
        else:
            print("vacancy list is empty yet")
        print("================end of report==================")

    def set_display_lines_dialog(self):
        """set maximum string for display information
        actual for print_ext_mode"""
        print("-----------------------")
        print("Enter maximum of lines for display")
        tmp_input = input(">")
        if len(tmp_input) > 0 and tmp_input.split()[0].isdigit():
            self.__max_count_object_print = int(tmp_input.split()[0])
        print(f"OK. now maximum of lines for display is {self.__max_count_object_print}")

    def set_filters_dialog(self):
        """dialog for setting filters
        actually I can extend this function, but ... I am so lazy =)))
        let it be with two arguments"""
        print("-----------------------")
        print("Enter keyword for filter display")
        tmp_input = input(">")
        self.filter_keyword = tmp_input
        print("Enter threshold for minimal salary filter display")
        tmp_input = input(">")
        if len(tmp_input) > 0 and tmp_input.split()[0].isdigit():
            self.filter_by_salary = int(tmp_input.split()[0])
        print(f"OK. now we will be filtered for {self.filter_keyword} with minimal salary {self.filter_by_salary}")

