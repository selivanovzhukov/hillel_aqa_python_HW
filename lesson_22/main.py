import random

import faker
from faker import Faker
from lesson_22 import models, crud_actions
from lesson_22.database import SessionLocal, engine
fake = Faker()

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

def populate_db():
    if db.query(models.Course).count() == 0:
        print("Initial data creating")
        course_names = [
            'Python QA Automation', 'JavaScript for Testers',
            'Performance Testing with JMeter', 'API Testing with Postman',
            'Mobile Automation with Appium'
        ]
        for course_name in course_names:
            courses = models.Course(name=course_name)
            db.add(courses)
        db.commit()

        first_name = fake.first_name()
        last_name = fake.last_name()

        courses = db.query(models.Course).all()
        for i in range(20):
            students = models.Student(first_name=first_name, last_name=last_name)
            num_courses = random.randint(1, 10)
            students.courses = random.sample(courses, num_courses)
            db.add(students)
        db.commit()
        print("Database populated successfully")
    else:
        print("Database already populated")


if __name__ == '__main__':
    populate_db()

    crud_actions.add_student_to_course(db, student_first_name=fake.first_name(), student_last_name=fake.last_name(), course_name="Python QA Automation")

    course_name = "Python QA Automation"
    course = crud_actions.get_student_courses(db, course_name)
    if course:
        print(f'\nStudents on course "{course_name}"')
        for student in course.students:
            print(f'\t{student.first_name} {student.last_name}')

    crud_actions.update_student_name(db, 1, new_first_name=fake.first_name(), new_last_name=fake.last_name())
    updated_student = crud_actions.get_course_for_student(db, 1)
    print(f'Student "{updated_student.first_name} {updated_student.last_name}" updated')

    student_id_to_delete = 5
    if crud_actions.delete_student(db, student_id_to_delete):
        print(f'Student "{student_id_to_delete}" deleted')
    else:
        print(f'Student "{student_id_to_delete}" not found')

    db.close()
