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








































