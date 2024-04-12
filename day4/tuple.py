# tuple is immutable which means once you create it

# you can't change its contents  imagine it as a fixed collection 
# of items like a snap shot of some data that you cant modify

# practice

my_tuple = (1,2,3)

print(type(my_tuple))

# # how to access tuple

print(my_tuple[0]
      )
print(my_tuple[1]
      )
print(my_tuple[2]
      )

# print(my_tuple[3])

# sorting coordinates
test = (10,20)
print(test)

#returning multiple value from a function
def get_name_and_age():
    name = "bharathi"
    age = "26"
    return(name,age)

result = get_name_and_age()

x,y = result

print(f"this is my name{x},this is my age {y}")

#grouping data

name_age_address = ("bharathi",26,"chennai tharamani")

print(name_age_address,"this is called grouping the data")


#iterating through pairs

fruit_basket = (("apple",5),("banana",10),("orange",8))

for fruit,quantity in fruit_basket:
    print(f"there are {quantity},{fruit}")



#passing immutable data to function 

def process_data(input_data):
    print(input_data)

input_data = (1,2,3,4,5,6,7,8)

process_data(input_data)