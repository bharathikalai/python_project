# for loop 


fruites = ["apple","banana","cherry","date"]

for fruite in fruites:
    print(fruite,"fruite")

numbers = [10,20,30,40,50]

sum_of_numbers = 0

for num in numbers:
    sum_of_numbers +=num

print("the sum of numbers is:",sum_of_numbers)



#for loop to manipulate data

text = "Hello world!"

letter_frequency = {}

text = text.lower()

for char in text:
    if char.isalpha():
        if char in letter_frequency:
            letter_frequency[char] +=1
        else:
            letter_frequency[char] = 1

print("letter frequencies:")
for letter, frequency in letter_frequency.items():
    print(f"{letter}: {frequency}")

print(letter_frequency.items,"the real value")









