from datetime import date

class Person:
    def __init__(self,name,birthyear):
        self.name = name
        self.birthyear = birthyear

    def age(self):
        today = date.today()
        return today.year - self.birthyear
    def is_adult(self):
        return self.age() >= 18
    
class Course:
    def __init__(self,cource_name,cource_code):

        self.course_name  = cource_name
        self.cource_code = cource_code
        self.students = []

    def enroll_student(self,student):
        self.students.append(student)

    def display_students(self):
        print(f"students enrolled in {self.course_name} ({self.cource_code})")
        for student in self.students:
            print(student.name)

class Student(Person):
    def __init__(self, name, birthyear,student_id):
        super().__init__(name, birthyear)
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_course(self,course):
        self.enrolled_courses.append(course)
        course.enroll_student(self)
    
    def display_enrolled_courses(self):
        for course in self.enrolled_courses:
            print(course.course_name)



#creating a instances of the course class

math_course = Course("Mathematics","Math101")
physics_cource = Course("Physics","PHYS102")

#creating an instance of the student class

student1 = Student("Alice",2000,"2022002")

#Enrolling student in courses

student1.enroll_course(math_course)
student1.enroll_course(physics_cource)


#displaying cources enrolled by student

student1.display_enrolled_courses()

#displaying students enrolled in each course

math_course.display_students()
physics_cource.display_students()