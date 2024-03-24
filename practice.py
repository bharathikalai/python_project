
# topic is try and exception

# try:
#     print(x)
# except:
#     print("an exception occured")



# try:
#     if a > 10:
#         print("i am trying to hack you")

# except:
#     print("bro are you ok")

# try:
#     print(x)
# except Exception as e:
#     print(e)



# import counter class from collections module
from collections import Counter

# Creation of a Counter Class object using 
# string as an iterable data container
x = Counter("geeksforgeeks")

print("counter check", x)

# printing the elements of counter object
for i in x.elements():
	print ( i, end = " ")