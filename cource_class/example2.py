class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    def enroll_studnet(self,student_name):
        self.students.append(student_name)


class Student:
    def __init__(self,name):
        self.name = name



math_course = Course("math")
physics_course = Course("physics")

student1 = Student("bharathi")
student2 = Student("kalai")

math_course.enroll_studnet(student1.name)
physics_course.enroll_studnet(student1.name)

