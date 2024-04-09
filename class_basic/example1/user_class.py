class User:
    users = 0 # class_variable
    def __init__(self,user_name,password):
        self.user_name = user_name   #instance variable
        self.password = password
        User.users+=1
    def register(self):
        print("user has been register"+self.user_name)
    def login(self):
        print("user has been login"+self.user_name)