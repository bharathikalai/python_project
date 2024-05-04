#hackers rank problem 1


# first try  

if __name__ == "__main__":
    N= int(input())
    a = []

    a.insert(0,5)
    a.insert(1,10)
    a.insert(0,6)
    print(a)
    a.remove(6)
    a.append(9)
    a.append(1)
    a.sort()
    print(a)
    a.pop()
    a.reverse()
    print(a)



# second try
my_list = []

n = int(input())

for _ in range(n):
    command = input().split()
    print(command,"the value of command")

    if command[0] == "insert":
        my_list.insert(0,5)
        my_list.insert(1,10)
        my_list.insert(0,6)
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        my_list.remove(6)
    elif command[0] == "append":
        my_list.append(9)
        my_list.append(1)
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()
    elif command[0] == "print":
        print(my_list)


#third try :



# Initialize an empty list
my_list = []

# Sample input
input_lines = [
    "12",
    "insert 0 5",
    "insert 1 10",
    "insert 0 6",
    "print",
    "remove 6",
    "append 9",
    "append 1",
    "sort",
    "print",
    "pop",
    "reverse",
    "print"
]

# Read in the value of n
n = int(input_lines[0])

# Process n lines of commands
for line in input_lines[1:]:

    print("line",line)
    command = line.split()  # Read a command and split it into parts

    print(command,"this is the command")
    # Check the command type
    if command[0] == "insert":
        index = int(command[1])
        value = int(command[2])
        my_list.insert(index, value)
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        value = int(command[1])
        my_list.remove(value)
    elif command[0] == "append":
        value = int(command[1])
        my_list.append(value)
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()





input_lines = [
    "12",
    "insert 0 5",
    "insert 1 10",
    "insert 0 6",
    "print",
    "remove 6",
    "append 9",
    "append 1",
    "sort",
    "print",
    "pop",
    "reverse",
    "print"
]



get = input_lines[1:]

print(get,"the value of get")





#final try this is the correct format


# Initialize an empty list
my_list = []

# Read the value of n
n = int(input())

# Read and process each command
for _ in range(n):
    command = input().split()
    
    if command[0] == "insert":
        my_list.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(my_list)
    elif command[0] == "remove":
        my_list.remove(int(command[1]))
    elif command[0] == "append":
        my_list.append(int(command[1]))
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()
