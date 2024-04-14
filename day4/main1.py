# another project in tuple


def main():
    students = []

    while True:
        print("\n1. Add Student")
        print("2. Calculate Grades")
        print("3. Exit")

        choice = input("enter your choice")

        if choice == "1":
            name = input("enter your name")
            grades = []
            while True:
                grade = input("enter students grade (q to quit)")
                if grade.lower() == 'q':
                    break
                else:
                    grades.append(float(grade))
                    print("grade",grades)

            students.append((name,grades))
            print(students,"students")
            print(f"{name } grades added successfully")

if __name__ == "__main__":
    main()