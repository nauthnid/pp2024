def input_student():
    students = {}
    num_students = int(input("Enter the number of students in class: "))
    for _ in range(num_students):
        id = input("Student ID: ")
        name = input("Fullname: ")
        dob = input("Date of birth: ")
        students[id] = (name, dob, {})
    return students

def input_course():
    courses = {}
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        id = input("Course ID: ")
        name = input("Course name: ")
        courses[id] = name
    return courses

def enter_mark(students, courses):
    while True:
        course_id = input("Enter course ID to input mark (q to quit): ")
        if course_id == 'q':
            break
        if course_id not in courses:
            print("Invalid course.")
            continue
        for student_id in students:
            mark = float(input(f"input mark for {students[student_id][0]}: "))
            students[student_id][2][course_id] = mark

def Display_course(courses):
    print("\nCourse Info:")
    print("{:<10} {:<15}".format('ID', 'Name'))
    for id, name in courses.items():
        print("{:<10} {:<15}".format(id, name))

def Display_student_info(students):
    print("\nStudent Info:")
    print("{:<10} {:<15} {:<15}".format('ID', 'Name', 'Date of Birth'))
    for id, info in students.items():
        print("{:<10} {:<15} {:<15}".format(id, info[0], info[1]))

def Display_mark(students, courses):
    print("\nMark:")
    for id, info in students.items():
        print(f"\nID: {id}, Name: {info[0]}")
        print("{:<10} {:<15}".format('Course', 'Mark'))
        for course_id, mark in info[2].items():
            print("{:<10} {:<15}".format(courses[course_id], mark))

def main():
    students = {}
    courses = {}

    while True:
    
        print("\n1. Enter student information")
        print("2. Enter course information")
        print("3. Enter mark")
        print("4. Display course")
        print("5. Display student")
        print("6. Display mark")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            students = input_student()
        elif choice == 2:
            courses = input_course()
        elif choice == 3:
            enter_mark(students, courses)
        elif choice == 4:
            Display_course(courses)
        elif choice == 5:
            Display_student_info(students)
        elif choice == 6:
            Display_mark(students, courses)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
students = []
courses = []

def input_students():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append((id, name, dob))

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((id, name))

def input_marks():
    course_id = input("Enter course id to input marks: ")
    for course in courses:
        if course[0] == course_id:
            for student in students:
                mark = input(f"Enter mark for student {student[1]}: ")
                student.append((course_id, mark))

def list_courses():
    for course in courses:
        print(course)

def list_students():
    for student in students:
        print(student)

def show_marks():
    course_id = input("Enter course id to show marks: ")
    for student in students:
        for i in range(3, len(student)):
            if student[i][0] == course_id:
                print(f"Student {student[1]} got {student[i][1]} in course {course_id}")
