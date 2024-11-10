# print(10>9)

# print(10 == 9)

# print(10 < 9)


# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

# print(bool("hello"))
# print(bool(15))

# x = "hello"
# y = 15

# print(bool(x))
# print(bool(y))



# print(bool("abc"))

# print(bool([1,2,3]))

# print(bool(124))

# print(bool(1,2,3))   error

# print(bool(False))
# print(bool(None))
# print(bool(""))
# print(bool(0))
# print(bool(()))
# print(bool({}))

# class myclass():
#     def __len__(self):
#         return 0
# my_obj = myclass()
# print(bool(my_obj))

# def myfunction():
#     return True

# print(myfunction())



# def myfunction():
#     return True

# if myfunction():
#     print("YES")
# else:
#     print("NO")


# x = 200

# print(type(x))

# print(isinstance(x,str))



# x = bool

# print(x)

# if x == True:
#     print("bool is true")
# else:
#     print("bool is not true ")



# number = 0

# while number < 5:
#     print(number)
#     number += 1


# elements = [1,2,3,4,5]

# for element in elements:
#     if element == 3:
#         break
#     print(element)


# def fun(value):
#     if value:
#         print("the data is valid ")
#     else:
#         print("the data is not valid")


# data_check = 10 > 5

# fun(data_check)



# print("a" == "a")


# print([1,2,3] == [1,2,3])

# a = {1,3,3}

# print(type(a))
# print(tuple(a) == (1,3))
# print("the value of a",a)


# operators

# a = 1 +2
# print("a",a)

# b = 1 - 1
# print(type(b))
# print(b)


# c = 7% 9

# print(c)





# thislist = ["apple","banana","cherry"]
# thislist[1] = "jello"

# print(thislist)
# thislist[2] = ""
# print(thislist)


# listing = ["my","name","is","bharathi","thasan","is"]

# # print(len(listing))

# print(listing.count("is"))

# thislist = ["apple","banana","cherry","ram","relly"]

# print(thislist[:10])

# thislist = ["apple","banana","cherry"]

# if "apple" in thislist:
#     print("yes apple is in this list")
# else:
#     print("no apple is not in this list")



# thislist = ["apple","banana","cherry"]

# thislist.insert(2,"gogyl")

# print(thislist,"insert")

# thislist.append("hello")

# print(thislist)


# thislist = ["apple","banana","cherry"]

# secondlist = ["apple","banana","cherry"]

# # hello = thislist + secondlist

# # print(hello)

# thislist.extend(secondlist)

# print(thislist)





# thislist = ["apple","banana","cherry"]

# thislist.remove("apple")
# print("the result",thislist)


# thislist.pop(-1)

# print(thislist)


# thislist.clear()

# print(thislist)

# value = ["apple","mango","orange"]

# for i in range(len(value)):
#     print(i,"the value of i")

# lenn = len(value)
# print(lenn)
# 
# for x in value:
#     print(x)



# thislist = ["apple","banana","cherry"]

# [print(x) for x in thislist]


# # list Comprehension
# fruite = ["apple","banana","cherry","kiwi","mango"]

# newlist = []

# for x in fruite:
#     if "y" in x:
#         newlist.append(x)
# print(newlist)

# tuple 


# mytuple = ("apple","banana","cherry")

# print(type(mytuple))


# seting = (1,2,2,3)
# print("the value of setting",seting)

# lenh = len((seting))
# print("the value of len",lenh)


# thistuple = ("apple",)
# print(type(thistuple))


# tuple1 = ("apple",1,False)

# print(type(tuple1))
# print("result",tuple1)



# thistuple = ("apple","cherry","gelly")

# print(thistuple[0:])
# print(thistuple[:-1])

# thistuple = ("apple","banana","cherry")

# if "appleaa" in thistuple:
#     print("apple in the tuple")
# else:
#     print("apple is not in the tuple")



# fruites = ("apple","banana","cherry")

# (green,yellow,red) = fruites

# print(red)


# fruites = ("apple","banana","cherry","strawberry","raspberry")

# (green,yellow,*red) = fruites


# print(red)






# def fub(thi):
#     return thi

# thistuple = ("apple","banana","cherry")

# result = fub(thistuple)

# print(result)

# for x in thistuple:
#     print(x)









# thistuple = ("apple","banana","cherry")

# for i in range(len(thistuple)):
#     print(i,"the range of my tuple")




# thistuple = ("apple","banana","cherry")

# i = 0

# while i < len(thistuple):
#     print(thistuple[i])
#     i +=1


# join the two tuple

# tuple1 = ("a","b","c")
# tuple2 = ("1","2","2")

# tuple3 = tuple1 + tuple2

# print(tuple3)


# # multiple the tuple 

# multiple = (1,2,3)

# multiply_with_3 = multiple * 2

# print("i am multiplying this",multiply_with_3)

# abc = (1,2,3,4,5)

# bc = abc.count(5)

# print("bc",bc)

# print(abc.count)

# cc = abc.index(3)

# print("the value of cc",cc)


# myset = {"apple","banana","cherry"}

# print("myset",myset)

# thisset = {"apple","banana","cherry",False,True,0}

# print(thisset)

# thisset = {"apple","banana","banana"}
# print(thisset)


# thisset = {"apple","banana","cherry"}

# for x in thisset:
#     print(x)

# print(thisset(1))

# items = {1,2,3}

# items.add(12345678)

# print(items)

# items.remove(3)
# print(items)


# thisset = {"apple","banana","cherry"}

# x = thisset.pop("apple")
# print("the value of x",x)



# set1 = {1,2,3}
# set2 = {1,2,3,"a"}

# set3 = set1.union(set2)

# print(set3)



# thisdict = {
#     "brand": "ford",
#     "model": "tata",
#     "year" : 1964
# } 

# print(len(thisdict))



# this = {
#     "list": ["red","yellow"],
#     "tuple": ("red",1)
# }

# print(len(this))


# print(this["list"][0])




#access the dict 



# x = {
#     "name":"bharathithasan",
#     "school": "krishnaswamy"
# }

# a = x.items()

# # print(type(a))

# print("the value of a",a)




# car = {
#     "brand":"ford",
#     "model":"mustang",
#     "year": 1997
# }

# car["year"] = "bharathi"

# print(car)






# thisdixt.pop("model")
# print(thisdixt)



# thisdixt.popitem()
# print(thisdixt)




# thisdixt = {
#     "brand":"ford",
#     "model":"mustang",
#     "year": 1964
# }



# for x ,y in thisdixt.items():
#     print(x,"the value of the x")
#     print(y,"the value of the y")


# copy 


# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year":88008
# }



# mydict = thisdict
# print(mydict)


# myfamily = {
#     "child1":{
#         "name":"lara",
#         "year": 123
#     },
#     "child2":{
#         "name":"raja",
#         "year": 12345
#     }
# }

# # print(myfamily)

# for x , obj in myfamily.items():
#     print(obj)

# for y in obj:
#     # print(y + ':',obj[y])
#     print(y )
#     print(obj[y])



# if statement


# def aa(a):
#     return print(a)

# a = 330
# b = 200

# if b > a:
#     print("b is greater than a")
# else:
#     aa("helo")


# a = 333
# b = 33

# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a anb b are equal")
# else:
#     print("a is greater than b")
# a = 19
# b = 1

# if a >b: print("a is graterthan b")



# a = 2
# b = 330

# print("A") if a > b else print("b")





# a = 330
# b = 3301
# print("A") if a > b else print("=") if a == b else print("B")


# a = 200
# b = 330
# c = 500

# if a > b or c > a:
#     print("both condition are true")



# a = 33
# b = 200

# if not a > b:
#     print("a is not greater than b")








# x = 1

# if x > 10:
#     print("above ten")
#     if x > 20:
#         print("and also above 20")
#     else:
#         print("but not above 20")


# while loop and for loop 

# i = 1

# while i < 6:
#     print(i)

#     i +=1




# i = 1

# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1



# i = 0 
# while i < 6:
#     i +=1
#     if i ==3:
#       continue
#     print(i)



# i = 1

# while i < 6:
#     print(i)

#     i +=1
# else:
#     print("i is no longer less than 6")



# fruits = ["apple","banana","cherry"]

# for x in fruits:
#     print(x)


# for x in "banana":
#     print("the value of x",x)

# x = ["banana","cherry","mango"]

# for y in x:
#     if y == "cherry":
#         continue
#     print(y) 
# for x in range(6):
#     print(x)


# for x in range(2,30,3):
#     print(x)







# else in for Loop  



# for x in range(6):
#     print(x)
# else:
#     print("finally finished")





# adj = ["red","big","tasty"]

# fruits = ["apple","banana","cherry"]


# for x in adj:
#     for y in fruits:
#         print(x)
#         print(y)





# pass statement


# for x in [0,1,2]:
#     print(x)


# creating a function

# def my_function():
#     print("hello from a function")

# my_function()




# def my_function(fname):
#     print(fname + " refsnes")

# my_function("email")
# my_function("tobias")
# my_function("linus")



#  no of argument


# def my_function(fname, lname):
#     print(fname + " " + lname)
# my_function("email","regsnes")




# arbitrary arguments *args



# def my_function(*kids):
#     print("the youngest child is "+ kids[2])



# my_function("bharathi","kurathi","surathi")



# key word arguments



# def my_function(child3, child2,child1):
#     print("the youngest child is " + child3)

# my_function(child1="mosas",child2="kali",child3="vutai")






# arbitrary keyword arguments , **kwargs


# def my_function(**kid):
#     print("his last name is "+ kid["lname"])

# my_function(fname = "tobi",lname = "vudi")



# default arguments



# def my_function(country = "norway"):
#     print("i am  from "+ country)

# my_function()
# my_function("swedan")
# my_function("india")
# my_function("brazil")



# def my_function(food):

#     for x in food:
#         print(x)


# fruits = ["apple","banana","cherry"]

# my_function(fruits)





# def my_function(x):
#     return 5 * x

# print(my_function(3))

# print(my_function(30))

# print(my_function(300))







# def  myfunction():
#     pass






# def my_function(x, /):
#     print(x)
# my_function(x= 2)


# def my_function(*, x):
#     print(x)

# my_function(3)


# def my_function(a,b,/, *, c, d):
#     print(a +b + c +d)
# my_function(5,7, c = 7,d = 8)






#recursion

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result 

# print("recursion example result")

# tri_recursion(6)



# def factorial(n):
#     if n == 0:  # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)  # Recursive call


# print(factorial(5))



# lambda


# x = lambda b : b + 10

# print(x(5))




# x = lambda a,b : a * b
# print(x (1,10))



# x = lambda a,b,c : a + b + c

# print(x(5,6,2))





# def myfunction(n):
#     return lambda a : a * n

# mydoubler = myfunction(2)

# print(mydoubler(11))




# array


# car1 = ["Ford"]

# car2 = "Volvo"

# car3 = "BMW"



# print(len(car1[0]))



# python classes and object

# class MyClass:
#     x = 5

# print(MyClass.x)


# class MyClass:
#     x = 5

# p1 = MyClass()

# print(p1.x)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("John",36)

# print(p1.age)
# print(p1.name)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("John",36)

# print(p1)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}{self.age}"



# p1 = Person("john",36)

# print(p1)





# object method


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("john",90)

# p1.myfunc()




# the self parameter 


# class Person:
#     def __init__(abc,name,age):
#         abc.name = name
#         abc.age = age
#     def myfun(abcaaa):
#         print("hello my name is "+ abcaaa.name)

# p1 = Person("bharathi",90)

# p1.myfun()


# python inheritance


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname,self.lname)

# x = Person("John","Doe")

# x.printname()



# iterators


# mytuple = ("apple","banana","cherry")

# myit = iter(mytuple)

# print(myit)

# # iterator vs iterable

# mytuple = ("apple","banana","cherry")

# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"

# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple = ("apple","banana","cherry")

# for x in mytuple:
#     print(x)

mytuple = "banana"

for x in mytuple:
    print("the value of the x",x)

































































































