class VacancyListView:

    def print_all(self, data):
        if data:
            for i in data:
                print(i)
        else:
            print("vacancy list is empty yet")
