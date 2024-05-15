#In Python, a string can be split on a delimiter.


#input


# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']

#output 

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 


def split_and_join(line):
    a = line.split(" ")

    a = "-".join(a)
    return a
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#in this code i am using two method one is split
# and another one is join

#by using splint we can split the data 

# by using join we can join the data