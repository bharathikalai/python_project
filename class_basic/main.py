# # try 1 

# class Car:
#     def __init__(self,mark,model,year):
#         self.make = mark
#         self.module = model    # here i am set the variable to self
#         self.year = year

#     def display_info(self):
#         print(f"this is a {self.year} {self.make} {self.module}")

# #creating an instance of the care class

# my_car = Car("Toyota","corolla",2020)  # here i am passing the argument to class

# my_car.display_info()    # here i am calling the function 




# try 2 

# multiplay devison and subraction 

# class Maths:
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2

#     def mulpi(self):
#         a = self.value1 
#         b = self.value2
#         c = a * b
#         return c
    
#     def sub(self):
#         a = self.value1
#         b = self.value2
#         c = a / b
#         return c

# value = Maths(1,2)

# c = value.mulpi()
# print("value for c",c)

# c = value.sub()
# print("value for c",c)


# try 3 

# class Rec():
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2 * (self.length + self.width)


# my_rec = Rec(5,3)


# print("Area:", my_rec.area())

# print("Perimeter:", my_rec.perimeter())



# try 4 : 
from datetime import date

class Person:

    def __init__(self,name,birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self):
        today = date.today()
        return today.year - self.birth_year
    
    def is_adult(self):
        return self.age() >=18
    
person1 = Person("bharathi",1997)

if person1.is_adult():
    print(f"{person1.name} is a adult.")
else:
    print(f"{person1.name} is not an adult")