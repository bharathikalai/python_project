class Course:
    def __init__(self,course_name):
        self.course_name = course_name


class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def enroll_course(self,course):
        self.courses.append(course)


math_course = Course("maths")
physics_course = Course("physics")

student1 = Student("bharathi")

student1.enroll_course(math_course)
student1.enroll_course(physics_course)

for course in student1.courses:
    print(course.course_name)




