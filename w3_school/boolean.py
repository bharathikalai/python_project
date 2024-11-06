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


# list Comprehension
fruite = ["apple","banana","cherry","kiwi","mango"]

newlist = []

for x in fruite:
    if "y" in x:
        newlist.append(x)
print(newlist)



