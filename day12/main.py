class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.next = None

class StudentRoster:
    def __init__(self):
        self.head = None
    def add_student(self,name,student_id):
        new_student = Student(name,student_id)
        new_student.next = self.head
        self.head = new_student
    def view_roster(self):
        current_student = self.head
        while current_student:
            print(f"student ID: {current_student.student_id} Name: {current_student.name}")
            current_student = current_student.next


def main():
    roster = StudentRoster()

    while True:
        print("\nStudent Roster Menu:")
        print("1. Add Student")
        print("2. View Roster")
        print("3. Search Roster")
        print("4. Exit")

        choice = input("Enter your choice")

        if choice == '1':
            name = input("enter student name: ")
            student_id = input("enter student id")
            roster.add_student(name,student_id)
        elif choice == '2':
            roster.view_roster()

if __name__ == "__main__":
    main()