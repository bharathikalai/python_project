class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model
        self.speed = 0
    def start(self):
        print(f"the {self.color} {self.model} care strats")
    def accelerate(self,speed_increase):
        self.speed +=speed_increase
        print(f"the {self.color}{self.model} car accelerates to {self.speed} mph")
    def stop(self):
        self.speed = 0
        print(f"the {self.color} {self.model} car stops")


#creating the object of the car class

car1 = Car("red","toyoto")
car2 =  Car("blue","honda")

car1.start()
car1.accelerate(30)
car1.accelerate(20)
car1.stop()

car2.start()
car2.accelerate(25)
car2.accelerate(10)
car2.stop()
car2.accelerate(25)
