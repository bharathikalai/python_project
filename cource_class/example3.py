class Course:
    def __init__(self,course_name):
        self.course_name = course_name

class Student:
    def __init__(self,name):
        self.name = name

math_course = Course("math")

student1 = Student("bharathi")

print(student1.name)

print(math_course.course_name)