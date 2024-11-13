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
    
#         return test
#     else:
#         return s

# aa = solve("hello   world  lol")
# print(aa)


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


# aa = solve("bharathi thasan")
# print("aa",aa)



