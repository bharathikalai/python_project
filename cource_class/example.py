class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    def enroll_student(self,student):
        self.students.append(student)


class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def enroll_course(self,course):
        self.courses.append(course)
        course.enroll_student(self)


math_course = Course("maths")
physics_course = Course("physics")

student1 = Student("Alice")

student1.enroll_course(math_course)
student1.enroll_course(physics_course)


# Displaying enrolled courses for the student
print(f"{student1.name} is enrolled in the following courses:")
for course in student1.courses:
    print(course.course_name)