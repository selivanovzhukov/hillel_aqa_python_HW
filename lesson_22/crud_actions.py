from sqlalchemy.orm import Session
from lesson_22 import models


def add_student_to_course(db: Session, student_first_name: str, student_last_name: str, course_name: str):
    student = db.query(models.Student).filter(
        student_first_name == models.Student.first_name,
        student_last_name == models.Student.last_name
    ).first()

    if not student:
        student = models.Student(first_name=student_first_name, last_name=student_last_name)
        db.add(student)
        db.commit()
        db.flush()

    course = db.query(models.Course).filter(course_name == models.Course.name).first()

    if course:
        if course not in student.courses:
            student.courses.append(course)
            db.commit()
            db.refresh(student)
            print(f'Student {student.first_name} {student.last_name} added to course {course.name}')
            return student
        else:
            db.rollback()
            print(f'Student {student.first_name} {student.last_name} already added to course {course.name}')
            return student
    else:
        db.rollback()
        print(f'Error: Course {course.name} does not exist')
        return None

def get_student_courses(db: Session, course_name: str):
    return db.query(models.Course).filter(course_name == models.Course.course_name).first()

def get_course_for_student(db: Session, student_id: int):
    return db.query(models.Student).filter(student_id == models.Student.id).first()

def update_student_name(db: Session, student_id: int, new_first_name: str, new_last_name: str):
    student = db.query(models.Student).filter(student_id == models.Student.id).first()
    if student:
        student.first_name = new_first_name
        student.last_name = new_last_name
        db.commit()
        db.refresh(student)
        print(f'Student {student.first_name} {student.last_name} updated')
        return student
    return None

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(student_id == models.Student.id).first()
    if student:
        db.delete(student)
        db.commit()
        return True
    return False


