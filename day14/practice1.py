# result = ["friends","lover","love","bitch"]

# print(len(result))






# a = len(['b', 'h', 'a', 'r', 'a', 't', 'h', 'i']) + len(['x'])
# print(a,"the value of a")


# count = 9

# # list of FLAMES acronym
# result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

# 	# keep looping until only one item
# 	# is not remaining in the result list
# while len(result) > 1:

#     # store that index value from
#     # where we have to perform slicing.
#     split_index = (count % len(result) - 1)

#     # this steps is done for performing
#     # anticlock-wise circular fashion counting.
#     if split_index >= 0:

#         # list slicing
#         right = result[split_index + 1:]

#         left = result[: split_index]

#         # list concatenation
#         result = right + left
#         print("result",result)

#     else:
#         result = result[: len(result) - 1]
#         print(result,"the real result")

# # print final result
# print("Relationship status :", result[0])


# a = ['Marriage', 'Enemy'] 

# b= a[0]
# print(b,"the print of b")





count = 5

result = ['a','b','c','d','f']

while len(result) > 1:
    si = (count%len(result) - 1)
    print("si",si)

    if si >=0:
        right = result[si + 1:]
        print("right",right)
        left = result[:si]
        print("left",left)

        result = right+ left
        print("result if",result)

    else:
        result = result[: len(result) -1]
        print("result else",result)
print(result)



# a = True

# while a:
#     a = True
#     # print("ABC")