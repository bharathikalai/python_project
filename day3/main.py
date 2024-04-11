#lets practics
def find_fact(num):  #my arug will recive here
    factors = []   # empty array variable

    for x in range(2,num+1):    

        while num % x == 0:
            factors.append(x)
            num //=x
    return factors


def main():
    num = int(input("eneter the number"))  # this is the input number
    factors = find_fact(num)  # call the function with arug 

    if len(factors) == 0:
        print("the number itself is prime")
    else:
        print(f"prime factors of {num} are {factors} ")


if __name__ == "__main__":
    main()


# def find_fact(num):

#     factors = []   # empty array variable

#     for x in range(2,num+1):   
#         print(x,"the value of x") 

#         while num % x == 0:
#             factors.append(x)
#             num //=x
#             print("num",num)
#     return factors

# x = find_fact(9)
# # the expected output of x is [2, 3]
# print(x)






