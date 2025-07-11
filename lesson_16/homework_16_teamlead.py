class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name} - Salary: {self.salary}'


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'{Employee.__str__(self)} - Department: {self.department}'


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f'{Employee.__str__(self)} - Programming language: {self.programming_language}'


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size
        self.department = department

    def __str__(self):
        return f'{Employee.__str__(self)} - Department: {self.department} - Programming language: {self.programming_language} - Team size: {self.team_size}'
