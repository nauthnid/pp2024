import input
import output

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
            input.input_students()
        elif option == 2:
            input.input_courses()
        elif option == 3:
            input.input_marks()
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
            break

if __name__ == "__main__":
    main()
