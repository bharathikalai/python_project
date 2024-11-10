# import platform

from module1 import person1

# import module1 as jk

# jk.greeting("bharathi")


# name = jk.person1["name"]

# print("the value of my name",name)

# x = platform.system()
# print("the value of the x",x)


# x = dir(platform)
# print("the value of the x",dir)

# a = person1["country"]

# print("the value of a",a)



import datetime

# x = datetime.datetime.now()

# print("the value of x",x)

# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(2020,5,17)

# print("the value of x",x)




# import datetime
# x = datetime.datetime(2018,6,1)

# print(x.strftime("%B"))





# python build in math

# x = min(5,10,25
#         )
# y = max(5,10,25)

# print("the value of x",x)
# print("the value of y",y)


# abs

# x = abs(-7.25)
# print("the value of x",x)




# x = pow(4,3)

# print("the value of x",x)




# the math module

# import math

# x = math.sqrt(64)

# print(x)





# import math
 
# x = math.ceil(1.4)

# y = math.floor(1.4)

# print("the value of the x",y)
# print("the value of the y",x)



# import math
# x = math.pi

# print("the value of the x",x)



# python json


# import json


# x = '{"name":"john","age":30,"city":"New York"}'

# print("the value of x",x)


# import json

# x = {
#     "name": "john",
#     "age": 30,
#     "city": "new york"
# }

# y = json.dumps(x)

# print(type(y))

# x = {
#     "name" : "John",
#     "age" : 30,
#     "married" : True,
#     "divorced" : False,
#     "children": ("Ann","Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230","mpg": 27.5},
#         {"model": "Ford Edge","mpg": 24.5}
#     ]
# }

# print("the value of x",x)

# print(json.dumps(x, indent=3, separators=(". ","=")))


# print(json.dumps(x, indent=3, sort_keys=True))



# {'name': 'John', 'age': 30, 'married': True, 'divorced': False, 'children': ('Ann', 'Billy'), 'pets': None, 'cars': [{'model': 'BMW 230', 'mpg': 27.5}, {'model': 'Ford Edge', 'mpg': 24.5}]}
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.5}]}

# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.5}]}
# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)




# if x:
#     print("yes match")
# else:
#     print("no it is not match")


# import re

# txt = "The rain in spain"
# x = re.split("ai",txt)

# print(x)


# txt = "The rain in spain"

# x = re.sub("\s","9",txt)

# print(x)



# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))



# python try except

# try
# except
# else
# finally

# try:
#     print(x)
# except:
#     print("an exception occurred")


# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")



# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")



# try:
#     result = 10 /0
# except ZeroDivisionError:

#     print("Oops you cant divide by zero")

# finally:
#     print("End of the program")


# Python User Input

# username = input("Enter username:")
# print("Username is " + username)



# String Formatting 

# txt = f"The price is 49 dollars"

# print(txt,"the output")

# price = 59 

# txt = f"The price is {price} dollars"

# print("txt",txt)



# prints = 59

# txt = f"The price is {prints:.2f} dollars"
# print("the value of txt",txt)


# txt = f"The price is {95:.2f} dollars"
# print("the value of txt",txt)


# txt = f"The price is {20 * 59} dollars"
# print("the value of txt",txt)

# price = 59 

# tax = 0.25

# txt = f"The price is {price + (price * tax)} dollars"

# price(txt)

# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)


# price = 49

# txt = f"It is very {'Expensive' if price>50 else 'cheap'}"
# print("the value of txt",txt)


# execute Funtion in F-Strings


# fruit = "apples"
# txt = f"I love {fruit.upper()}"
# print("the value of txt",txt)



# def myconverter(x):
#     return x * 0.3048

# txt = f"the plan is flying at a {myconverter(3000)} meter altitude"


# print("the value of txt",txt)





# more modifiers



price = 59000

txt = f"The price is {price:,} dollars"
print("the value of txt",txt)




















































































































