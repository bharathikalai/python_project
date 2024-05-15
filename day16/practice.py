import random


def  getDigits(num):
    return [int(i) for i in str(num)]


def noDuplicates(num):
    num_li = getDigits(num)
    print("the value of num_li",num_li)

    if len(num_li) == len(set(num_li)):
        print(len(num_li))
        print(len(set(num_li)))
        return True
    else:
        print("else")
        return False

def generateNum():
    while True:
        num = random.randint(10,20)
        if noDuplicates(num):
            print(noDuplicates(num))
            return num
        
def numOfBullsCows(num,guess):
    bulls_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i,j in zip(num_li,guess_li):
        if j in num_li:
            if j == i:
                print(j,i,"the value of j and i")
                bulls_cow[0] += 1
                print(bulls_cow[0] ,"fghjklkjhgfdfghjklkjhgf")
            else:
                bulls_cow[1] += 1
                print("else")
    return bulls_cow


num = generateNum()
print("the value of num",num)


tries = int(input("enter number of tries: "))

while tries > 0:
    guess = int(input("enter your guess: "))
    if not noDuplicates(guess):
        print("number should not have repeated digits try again")
        continue
    if guess < 10 or guess > 20:
        print("enter 2 digit number only try again..")
        continue

    bulls_cow = numOfBullsCows(num,guess)
    print(f"{bulls_cow[0]} bulls,{bulls_cow[1]} cows")
    tries -=1
    if bulls_cow[0] == 2:
        print("you guessed right!")
        break

else:
    print(f"you ran out of  tries Number was {num}")






# # continue


# # numbers = [1,2,3,4,5,6,7,8,9,10]

# # for num in numbers:
# #     if num % 2 == 0:
# #         continue
# #     print(num)




# num_li = [1,2,3,4]

# guess_li = [5,6,7,8]


# for i,j in zip(num_li,guess_li):
#     print("the value of i",i)
#     print("the value of j",j)


# num_li = [1,2,3,4]
# guess_li = [4,5,6,7,8]

# result = zip(num_li,guess_li)

# print(list(result))