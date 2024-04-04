from user import User,Student,Faculty

user1 = User("bharathi","P@ssw0rd")
user2 = User("kalai","zzzzz")
user3 = User("uma","abc")

user1.register()
user1.login()

print(user1.user_name)

print(User.user)



student1 = Student()

student1.geet_student()

fac1 = Faculty()
fac1.geet_student()

student1.login()