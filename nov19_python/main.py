#size 3  >> inout
#  >> output


# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------








size = 3
    # your code goes here
alphabet = "abcdefghijklmnopqrstuvwxyz"


my_list = []
    
for i in range(size):
        s = "-".join(alphabet[size - 1 : size - 1 - i : -1] + alphabet[size - i - 1: size])

        my_list.append(s.center(4 * size - 3, "-"))
        break
    
print("\n".join(my_list + my_list[-2::-1]))
        




a =  [10, 20, 30, 40, 50]

result = a[-2::-4]
print("result",result)