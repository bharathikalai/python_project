class User:
    user = 0
    def __init__(self,user_name,pwd):
        self.user_name = user_name  #this is called instance variable
        self.pwd = pwd
        User.user +=1

    def  register(self):
        print("Registering...." )

    def login(self):
        print("logging in ..." )

class Student(User):     # student class inherits user class
    def geet_student(self):
        print("Hi student")
        #user is parent class and student class is child class

class Faculty(User):     # student class inherits user class
    def geet_student(self):
        print("hello Teacher")


class temp(Faculty):
    def test(self):
        print("mulilevel ingeritance")
#multiple inheritance

class muliple_inheritance(Faculty,temp):
    print("multiple inheritance")

#method overwriting:




