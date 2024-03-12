import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def input_mark(self, course, mark, credit):
        self.marks[course] = (math.floor(mark * 10) / 10, credit)

    def calculate_gpa(self):
        if not self.marks:
            self.gpa = 0
        else:
            total_marks = np.array([mark for mark, credit in self.marks.values()])
            total_credits = np.array([credit for mark, credit in self.marks.values()])
            self.gpa = np.average(total_marks, weights=total_credits)

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

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

def list_courses():
    for course in courses:
        print(course.name)

def list_students():
    for student in students:
        print(student.name)

def show_marks():
    course_id = input("Enter course id to show marks: ")
    for course in courses:
        if course.id == course_id:
            for student in students:
                if course in student.marks:
                    print(f"Student {student.name} got {student.marks[course][0]} in course {course.name}")

def calculate_gpa():
    student_id = input("Enter student id to calculate GPA: ")
    for student in students:
        if student.id == student_id:
            student.calculate_gpa()
            print(f"Student {student.name} has a GPA of {student.gpa}")

def sort_students():
    students.sort(key=lambda student: student.gpa, reverse=True)
    for student in students:
        print(f"Student {student.name} with GPA {student.gpa}")

def main():
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Calculate GPA")
        print("8. Sort students by GPA")
        print("9. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            input_students()
        elif option == 2:
            input_courses()
        elif option == 3:
            input_marks()
        elif option == 4:
            list_courses()
        elif option == 5:
            list_students()
        elif option == 6:
            show_marks()
        elif option == 7:
            calculate_gpa()
        elif option == 8:
            sort_students()
        elif option == 9:
            break

if __name__ == "__main__":
    main()




