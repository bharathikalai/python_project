# # for loop 


# fruites = ["apple","banana","cherry","date"]

# for fruite in fruites:
#     print(fruite,"fruite")

# numbers = [10,20,30,40,50]

# sum_of_numbers = 0

# for num in numbers:
#     sum_of_numbers +=num

# print("the sum of numbers is:",sum_of_numbers)



# #for loop to manipulate data

# text = "Hello world!"

# letter_frequency = {}

# text = text.lower()

# for char in text:
#     if char.isalpha():
#         if char in letter_frequency:
#             letter_frequency[char] +=1
#         else:
#             letter_frequency[char] = 1

# print("letter frequencies:")
# for letter, frequency in letter_frequency.items():
#     print(f"{letter}: {frequency}")

# print(letter_frequency.items,"the real value")




# The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.


#find the prime numbers within a give range

start = 10
end = 50

print(f"prime numbers between {start} and {end} are:")
for num in range(start,end+1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):





