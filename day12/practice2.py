class Oldboy:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class Newboy:
    def __init__(self):
        self.head = None
    def add_boys(self,name):
        boy = Oldboy(name)
        boy.next = self.head
        self.head = boy
    def display_boy(self):
        b = self.head

        while b:
            print(b.data)
            b=b.next

all_boy = Newboy()

all_boy.add_boys("varun")
all_boy.add_boys("chandru")
all_boy.add_boys("raja")

all_boy.display_boy()
