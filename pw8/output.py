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
