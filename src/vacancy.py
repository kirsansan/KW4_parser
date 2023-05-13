class Vacancy:

    def __init__(self, title="non title", desc="non description", salary_from=0, salary_to=0, url="non url"):
        self.title = title
        self.description = desc
        self.salary_min: int = salary_from
        self.salary_max: int = salary_to
        self.url = url

    def __str__(self):
        return f"{self.title} with salary from {self.salary_min} to {self.salary_max}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', {self.salary_min}-{self.salary_max}, {self.url})"

    def __gt__(self, other):
        self.check_empty_salary()
        other.check_empty_salary()
        if self.salary_min > other.salary_min:
            return True
        if self.salary_min == other.salary_min:
            if self.salary_max > other.salary_max:
                return True
        return False

    def __ge__(self, other):
        if self.salary_min >= other.salary_min and self.salary_min != 0:
            return True
        else:
            if self.salary_max >= other.salary_max and self.salary_max != 0:
                return True
            return False

    def __lt__(self, other):
        self.check_empty_salary()
        other.check_empty_salary()
        if self.salary_min < other.salary_min:
            return True
        if self.salary_min == other.salary_min:
            if self.salary_max < other.salary_max:
                return True
        return False

    def __le__(self, other):
        if self.salary_min <= other.salary_min:
            return True
        return False

    def __eq__(self, other):
        if self.salary_min == other.salary_min and self.salary_max == other.salary_max:
            return True
        return False

    def get_json(self):
        return {"title": self.title,
                "description": self.description,
                "salary_min": self.salary_min,
                "salary_max": self.salary_max,
                "url": self.url
                }

    def check_empty_salary(self):
        if not self.salary_min:
            self.salary_min = 0
        if not self.salary_max:
            self.salary_max = 0
