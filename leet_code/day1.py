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