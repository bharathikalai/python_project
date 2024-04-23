class TrainCar:
    def __init__(self,cargo):
        self.cargo = cargo
        self.next = None

class Train:
    def __init__(self):
        self.head = None
    def attach_car(self,cargo):
        new_car = TrainCar(cargo)
        new_car.next = self.head
        self.head = new_car
    def display_train(self):
        current_car = self.head
        while current_car:
            print(current_car.cargo)
            current_car  = current_car.next
        print("none")



my_train = Train()

my_train.attach_car("passenger 1")
my_train.attach_car("passenger 2")
my_train.attach_car("passenger 3")

#displaying the tarin
print("initial train configuration:")
my_train.display_train()

my_train.attach_car("passenger 4 (new)")

print("\nTrain after adding a new passenger to the front:")

my_train.display_train()