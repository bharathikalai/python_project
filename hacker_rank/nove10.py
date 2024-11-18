# Chris Alan

# chris alan





# input = input()

# input = "bharathi thasan"

# if len(input) <= 1000:
#     for x in input:
#         print(input[0] == input.islower())

#         if input[0] == input.islower():
#             firstletter = input.upper()
#             print(firstletter)
#         else:
#             print("hello")


# a = "dfghjkllo bja" 
# text = ""

# for x in a:
#     if (a[0].lower()):
#         first = (a[0].upper())
#         text += first
#         break
# for y in a[1:]:
#         text += y
# print(text)

# def solve(s):
    
#     if len(s) <= 1000 and s.alphabet():
        
#         return s.title()
#     else:
#         return s

# bharathi = solve("1bhrathi thasan")

# # print(bharathi)


# def tester(name):
#     if len(name) <= 1000  and type(name) == str:

#         return name.title()

#     else:
#         return name



# name = "bharathi thasan  6h"

# result = tester(name)
# print(result)



# name = "Bhratahi thasan"

# resul = name.split()



# test = ""
# for x in resul:
#     result = x.capitalize()
#     test += result
# print(test)
    



# def solve(s):
    
#     if len(s) <= 1000:
#         sp = s.split()
#         test = ""
#         for x in sp:
#             result = x.capitalize()
#             test += result  
#             test += " "   
    
# #         return test
# #     else:
# #         return s

# # aa = solve("hello   world  lol")
# # print(aa)


# def solve(s):
#     result = ""
#     capitalize_next = True

#     for char in s:
#         if char == " ":
#             result += char
#             capitalize_next = True
#         elif capitalize_next and char.isalpha():
#             result += char.upper()
#             capitalize_next = False
#         else:
#             result += char
#             capitalize_next = False
#     return result


# aa = solve("bharathi thasan     am ji   6h")
# print("aa",aa)



# d






# def new_function(thename):
#     change = True
#     text = ""
#     for x in the_name:
#         if x == " ":
#             text +=x
#             change = True 
#         elif change and x.isalpha():
#             text += x.upper()
#             change = False
#         else:
#             text +=x
#             change = False
#     return text




# the_name = "bharathi thasan"


# result = new_function(the_name)

# print(result)



# make add and even 



# def add_even(nqqq):

#     if nqqq % 2 == 0:
#        return print("it is even")
#     else:
#        return print("it is add")
        

# nqqq = int(input())

# result = add_even(nqqq)

# num1 = 40
# num2 = 30


# if num1 * num2 <= 1000:
#     print(num1* num2)
# else:
#      s = num1 + num2

#      print("the value of s",s)





# num = 10

# previous = 0

# for x in range(10):
#     print(f"current number {x} previous {previous}")

#     previous = x


# text = "PYnative"
# eve = ""

# for x in text[0::2]:
#     print(x)



# text = "bharathi"

# size  = len(text)

# for x in range(0,size -5,2):
#     print(x)








# name = "Bharathithasan"

# a = name[:5]
# print(type(a))





# username = "bharathithasan"
# number = 3

# print(username[number:])




# exercise

# check the first and last number of the list are same

# numbers_x = [10,20,30,40,100]

# if numbers_x[0] == numbers_x[-1]:
#     print("first and last number of list are same"
#     )
# else:
#     print("first and last number of list is not same")



# exercise  display number divisible by 5


# def check_function(userinput):
#     value_5 = []
#     value_none = []
    
#     for x in userinput:
#         if x % 5 == 0: 
#           print(x)
#         elif x % 5 != 0:
#           print(x)


# userinput = [10,5,90,77,707,77]

# result = check_function(userinput)

# print(result)








# find the number of occurrences of a substring in a string


# str_x = "Emma is good developer. Emma is a writer"

# a = str_x.count("Emma")

# print("the value of a",a)



# without using string method


# def count_emma(statement):
#     count = 0

#     for i in range(len(statement) -1):
#         count += statement[i: ]






# count = count_emma("Emma is good developer. Emma is a writer")

# print(count)




# str_x = "Emma is good developer. Emma is a writer"

# print(str_x[0:4])
# print(len(str_x))






# for x in range(len(str_x) -1 ):
#     print(x)




# print the following pattern

# x = 5

# for x in range(1,x+1):
#     for  y in range(1,x+1):
#         print(x, end = " ")
    
#     print("\n")


#exercise 9 : check palindrome number



# userinput = int(input())



# if userinput % 11 == 0:
#     print("is a palindrome number ")

# else:
#     print("it is not a palindrome number")








# def palindrome(number):
#     print("original number",number)
#     original_num = number

#     reverse_num = 0

#     print("reverse_num",reverse_num)

#     while number > 0:
#         reminder = number % 10
#         reverse_number = (reverse_num * 10) + reminder
#         print(reverse_number)
#         number = number // 10

#     if original_num == reverse_num:
#         print("given number palindrome")
#     else:
#         print("given number is not palindrome")



# palindrome(121)
# # palindrome(125)


# def palindrome(number):
#     print("original number", number)
#     original_num = number
    
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10
#         print("number",number)
#         print("reverse_num",reverse_num)


#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")

# palindrome(121)
# # palindrome(125)







# exercise 10 : merge two list using the following condtion


# list1 = [10,20,25,30,35]
# list2 = [40,45,60,75,90]


# list = []

# for x in list1:
#     print(x)
#     if x % 2 != 0:
#         list +=x
# print(list)




# def merge_list(list1,list2):
#     result_list = []

#     for num in list1:
#         if num % 2 != 0:
#             result_list.append(num)
#     for num in list2:
#         if num % 2 == 0:
#             result_list.append(num)
    
#     return result_list





# list1 = [10,20,25,30,35]

# list2 = [40,45,60,75,90]

# print("result list", merge_list(list1,list2))







# exercise 11 

# get each digit from a number in the reverse order



# for example if the given integer umber is 7536 the output shall be 6 3 5 7 
# with a space separating the digit




# def reverse_order(userinput):
#     for x in userinput:
#         print(x)






# userinput = int(input())

# result = reverse_order(userinput)

# print(result)





# iii = 7536

# sst = str(iii)


# for x in sst:
#     xf = sst[-1]

#     print(xf)

    

number = 7536

print("given number ", number)

while number > 0:
    digit = number % 10

    print(digit,"digit")

    number = number // 10

    print(number,"number")

    print(digit,end = "")










b = "1234567"

for x in b:
    print("the value of x",x)




a = 1

for x in a:
    print(x)

