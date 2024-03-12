import os
import gzip
import pickle
import input
import output

def save_data(students, courses):
    with gzip.open('students.dat.gz', 'wb') as f:
        pickle.dump((students, courses), f)

def load_data():
    if os.path.exists('students.dat.gz'):
        with gzip.open('students.dat.gz', 'rb') as f:
            students, courses = pickle.load(f)
    else:
        students, courses = [], []
    return students, courses

def main():
    students, courses = load_data()
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
            input.input_students()
            save_data(students, courses)
        elif option == 2:
            input.input_courses()
            save_data(students, courses)
        elif option == 3:
            input.input_marks()
            save_data(students, courses)
        elif option == 4:
            output.list_courses()
        elif option == 5:
            output.list_students()
        elif option == 6:
            output.show_marks()
        elif option == 7:
            output.calculate_gpa()
        elif option == 8:
            output.sort_students()
        elif option == 9:
            save_data(students, courses)
            break

if __name__ == "__main__":
    main()

