class Student:
    def __init__(self, firstname, lastname, age, average_score):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.average_score = average_score

    def student_info(self):
        return self.firstname, self.lastname, self.age, self.average_score


    def average_score_edit(self, score):
        self.average_score += score


some_student = Student('Harry', 'Potter', 11, 50)
Student.average_score_edit(some_student, 5)
print(some_student.student_info())

