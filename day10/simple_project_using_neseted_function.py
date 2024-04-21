def welcome_message(name):
    def get_greeting():
        return "hello"
    def get_message():
        return f"{get_greeting()},{name}! welcome to our program"
    
    return get_message()


user_name = input("enter your name:")
message = welcome_message(user_name)
print(message)
