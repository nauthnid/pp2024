class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_mark(self, course, mark):
        self.marks[course] = mark

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

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
        courses.append(Course(id, name))

def input_marks():
    course_id = input("Enter course id to input marks: ")
    for course in courses:
        if course.id == course_id:
            for student in students:
                mark = input(f"Enter mark for student {student.name}: ")
                student.input_mark(course, mark)

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
                    print(f"Student {student.name} got {student.marks[course]} in course {course.name}")

def main():
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Exit")
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
            break

if __name__ == "__main__":
    main()
