
class VacancyController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def print_all(self):
        return self.view.print_all(self.model.all)

