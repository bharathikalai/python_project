# task

# In Python, a string of text can be aligned left, right and center.

# sample input

# the sample input is 5

# sample output 

#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 




# width = 4

# print("".ljust(width,"-"))

# print("".rjust(width,"-"))

# print("h".center(width,"-"))


# def magic_function(sample_int):









# if __name__ == "__main__":
#     sample_int = 5

#     magic_function(sample_int)




#   h
#  hhh
# hhhhh
# hhhhhhh
# hhhhhhhhh


#first itteration 

# 0 + 1 = 1
# 1 + 2 = 3
# 2 + 3 = 5

# 3 + 4 = 7

# 4 + 5 = 9


# a = "a"

# b = a * 2

# print(b)

#sample output 
# >>> width = 20
# >>> print 'HackerRank'.center(width,'-')
# -----HackerRank-----

# width = 5 
# a = "H"
# print(a.center(width,"-"))




# for x in range(width):
#     c = width + x 
#     b = x + 1 + x
#     a = "H"*b

#     print(a.center(c, "-"))

# this methdo failed dont follow this method
n = 5
for i in range(1, n + 1):
    print(("H" * (2 * i -1)).center(2 * n - 1))

for i in range(1 , n+2):
    print(("H" * (5)).center(2 * n - 1) + ("H" * (5)).center(5 * n +3))

for i in range(1 , n-1):
    print(("H" * (27)).center(6 * n + 1))

for i in range(1 , n+2):
    print(("H" * (5)).center(2 * n - 1) + ("H" * (5)).center(5 * n + 3))

for i in range(1, n + 1):
    print(("H" * (9 - i + i )).center(10 * n + 3))


#   HHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHH   



#method 2  this method also wrong

# width = 20

# print("H".center(width," "))



n = 5


for i in (range(1,n+1)):
    print(("H"*(i + i - 1)).center(2*n -1))
for i in (range(1,n+2)):
    print(("H"*(n)).center(2*n -1) + ("H"*(n)).center(6*n -6))

for i in (range(1,n-1)):
    print(("H"*(n*n)).center(6*n -1))

for i in (range(1,n+2)):
    print(("H"*(n)).center(2*n -1) + ("H"*(n)).center(6*n -6))

for i in range(1, n + 1):
    print(("H" * (2 * n - (i + i - 1))).center(8 * n ))




#method 3 
#first itteration suppose to be like this

# n = 5

# print("h".center(9,"-"))

# print("hhh".center(9,"-"))

# print("hhhhh".center(9,"-"))

# print("hhhhhhh".center(9,"-"))

# print("hhhhhhhhh".center(9,"-"))   # this is the basement 


# first itteration 

n = 5
for i in range(1 , n+1):
    print(("H"*(2*i-1)).center(2 *n -1))

for i in range(1, n+2):
    print(("H"*(n)).center(n*2)+("H"*(n)).center(n*4))

for i in range(1,n-1):
    print(("H"*(n*n)).rjust(n*n+1))

for i in range(1, n+2):
    print(("H"*(n)).center(n*2)+("H"*(n)).center(n*4))

for i in range(1 , n+1):
    print(("H"*(2*n-(i+i-1))).rjust(n*n-i))





























