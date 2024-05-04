##########question#########
# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters
# and vice versa.


#######for example###########


# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  


########Function Description##############3

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string 



# final output code 

def swqp_case(s):

    final = ""

    for x in s:
        if x.islower():
            final +=x.upper()
        else:
            final +=x.lower()
    return final


if __name__ == "__main__":
    s = input()
    final_output = swqp_case(s)

    print(final_output)



# a = "bHratahy"
# b = a.lower()
# print(b)
# c = a.upper()


#these two method i am using one is lower and another one is upper 

# lower method is for convert lower letter to caps letter
# uppper method is for convert caps letter to small letter(lowerletter)



