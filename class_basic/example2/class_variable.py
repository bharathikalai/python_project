#inherits

#type of inherits

#type 1 muliplilevel inherits
#type 2 multiple inherits


class User:
    def __init__(self,user_name,user_password,user_roll_no):
        self.user_name = user_name
        self.user_password = user_password
        self.user_roll_no = user_roll_no
    def school(self):
        print(f"hai {self.user_name} welcome to the school")
    def collage(self):
        print(f"welcome {self.user_roll_no} this is your collage roll no")

class Games(User):
    def cricket():
        print("you have chossed cricket game")

class Food:
    def __init__(self, user_name, user_password, user_roll_no,food_name):
        super().__init__(user_name, user_password, user_roll_no,food_name)
        self.food_name = food_name
    def food(self):
        print("do you like any food"+self.food_name)


class All(Games,Food):
    pass
