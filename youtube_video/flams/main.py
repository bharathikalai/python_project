# first thing user input     # first has been successfully completed

# this is second this eliminate the mached letter


# third :   f l a m e s   count


# 4 thing is a calculation  

# final result l final result is going to be 1


def eliminate(user1,user2):

    for i in range(len(user1)):
        for j in range(len(user2)):
            if user1[i] == user2[j]:
                c = user1[i]
                user1.remove(c)
                user2.remove(c)

                user = user1 + ["*"] + user2
                return [user,True]
            
    user = user1 + ["*"] + user2
    return [user,False]



if __name__ == "__main__":

    user1 = input("enter your name")
    user1 = user1.lower()
    user1 = user1.replace(" ","")
    user1 = list(user1)

    user2 = input("enter your name")
    user2 = user2.lower()
    user2 = user2.replace(" ","")
    user2 = list(user1)
    print(user2,"user 2")

    process = True
    while process:
        output_elminate = eliminate(user1,user2)
        process = output_elminate[1]
        user = output_elminate[0]

        index_number = user.index("*")

        user1 = user[:index_number]
        user2 = user[index_number+1:]

    count = len(user1) + len(user2)

    result = ["f","l","a","m","e","s"]

    while len(result) > 1:

        split = count % len(result) - 1
        split = 0
        if split >= 0:

            # list slicing
            right = result[split + 1:]
            print("value right",right)
            left = result[: split]
            print("value left",left)

            # list concatenation
            result = right + left

        else:
            result = result[: len(result) - 1]

# # print final result
# print("Relationship status :", result[0])



# user 1 = vijy
# user 2 = slu 

# user = 8 

# result = 6

# result = f l a m e s
















