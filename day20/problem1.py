# Question

# In this challenge, the user enters a string and 
# a substring. You have to print the number of 
# times that the substring occurs in the given string. 
# String traversal will take place from left to right,
# not from right to left.


# NOTE: String letters are case-sensitive.


# Input Format

# The first line of input contains the 
# original string. The next line contains
# the substring.



# strinp function is user for to remove extra white space
# example  
# a = input().strip()

# print("the value of a",a)


#sample input and output 

#input 
# ABCDCDC
# CDC

#output 

# 2



#method 1

# def count_substring(string, sub_string):
#     mod  = len(string) % len(sub_string)
#     print("mod",mod)

#     sub = len(sub_string) + 1
#     print("sub value",sub)
#     d = string[sub:]

#     e = len(d)

#     e = e -1

#     f = string[e:len(string)- e]

#     c = list(d.split(" ")) + list(f.split(" "))

#     return len(c)

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


#method 2

a = "ThIsisaCoNfUsInG"


b = "isa"




for x in range(0,len(a)):
    if b in a:
        print(a.count(b))