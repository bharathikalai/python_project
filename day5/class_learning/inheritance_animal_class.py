class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woff")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow")



dog = Dog("bharathi")

cat = Cat("kalai")


dog.eat()

cat.meow()