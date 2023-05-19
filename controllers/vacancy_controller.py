from models.vacancy_model import VacancyModel
from view.vacancy_list_view import VacancyListView


class VacancyController:

    def __init__(self, model: VacancyModel, view: VacancyListView):
        self.model = model
        self.view = view

    def print_all(self):
        """Print all information"""
        return self.view.print_all(self.model.all)

    def print_ext(self):
        """Print extended mode"""
        return self.view.print_ext_mode(self.model.all)

    def set_and_print_select(self):
        """set filters for data before printing"""
        self.view.set_filters_dialog()
        prepared_for_print = self.model.filter_by_strings(self.view.filter_keyword.split())
        prepared_for_print = self.model.filter_by_salary(self.view.filter_by_salary, prepared_for_print)
        self.view.print_ext_mode(prepared_for_print)
        return
