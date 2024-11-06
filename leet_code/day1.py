class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woff"
    
    def dogs_year(self):
        return self.age
    


my_dog = Dog("bharathi",8)

print(my_dog.name)

print(my_dog.age)

print(my_dog.bark())

print(my_dog.dogs_year())




class test:
    def __init__(self,my_name,my_phone_number):
        self.my_name = my_name
        self.my_phone_number = my_phone_number

    def call_my_name(self):
        return print(self.my_name)
    
    def phone_number(self):
        return print(self.my_phone_number)
    

final = test("bharathi",9234567890)

final.call_my_name()
final.phone_number()




