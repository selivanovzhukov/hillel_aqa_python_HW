from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from lesson_22.database import Base

student_course_table = Table('student_course_table', Base.metadata,
                             Column('student_id', Integer, ForeignKey('student.id')),
                             Column('course_id', Integer, ForeignKey('course.id'))
                             )




class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    courses = relationship(
        'Course',
        secondary=student_course_table,
        back_populates='students',
        primaryjoin=id == student_course_table.c.student_id,
        secondaryjoin='Course.id == student_course_table.c.course_id'
    )
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    students = relationship(
        'Student',
        secondary=student_course_table,
        back_populates='courses',
        primaryjoin=id == student_course_table.c.course_id,
        secondaryjoin='Student.id == student_course_table.c.student_id'
    )
