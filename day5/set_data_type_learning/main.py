#what is set 

# set is a unorder collection of unique elements

#set s are mutable meaning you can add or remove elements from them 
# perorming mathematical set opertaions such as union intersection and 
#symmetric diffrence

#creating a set

my_set = {1,2,3,4,5}

print(type(my_set))

my_set = {1,2,3,4,5}    #  by using set we can remove the duplicate value

print("my_Set",my_set)  

# this output is 1 2 3 4 5   it removed the duplicate value

# i am adding the element to my_set
# by using add method we can add the new value in my_set
# my_set.add(6)
# my_set.add(7)
# print("my_set",my_set)


my_set.remove(6)
print(my_set,"my_set")


#union 

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}

union = set_1.union(set_2)

print("union",union)

#intersection

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}

intersection = set_1.intersection(set_2)

print("intersection",intersection)


#difference

diffrence = set_2.difference(set_1)
print("diffrence",diffrence)


#symmetric difference

symmetric_difference = set_1.symmetric_difference(set_2)

print("symmetric difference",symmetric_difference)