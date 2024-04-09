class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    def enroll_student(self,student_name):
        self.students.append(student_name)
        
        

english_course = Course("English")

english_course.enroll_student("bharathi")
english_course.enroll_student("kalai")
english_course.enroll_student("bk")

print(english_course.students)