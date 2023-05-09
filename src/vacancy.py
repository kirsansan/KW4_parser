class Vacancy:

    def __init__(self, title="non title", desc="non description", salary=0, url="non url"):
        self.title = title
        self.description = desc
        self.salary: int = salary
        self.url = url

    def __str__(self):
        return f"{self.title} with salary {self.salary}"

    def __str__(self):
        return f"{self.__class__.__name__}('{self.title}', {self.salary})"

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        return False

    def __ge__(self, other):
        if self.salary >= other.salary:
            return True
        return False

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        return False

    def __le__(self, other):
        if self.salary <= other.salary:
            return True
        return False

    def __eq__(self, other):
        if self.salary == other.salary:
            return True
        return False