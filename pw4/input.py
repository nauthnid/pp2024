from domains.student import Student
from domains.course import Course

students = []
courses = []

def input_students():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append(Student(id, name, dob))

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        courses.append(Course(id, name, credit))

def input_marks():
    course_id = input("Enter course id to input marks: ")
    for course in courses:
        if course.id == course_id:
            for student in students:
                mark = float(input(f"Enter mark for student {student.name}: "))
                student.input_mark(course, mark, course.credit)
