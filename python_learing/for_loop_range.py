# for i in range(0,5):
#     print(i)



n = "1234"  # The number you're comparing against
num = "1256"  # The number you're comparing to
count = 0  # Counter for the number of correct digits
correct = ['X']*4 # List to store correct digits, initialized with 'X's

# Loop through each digit position
for i in range(0, 4):
    # Check if the digit at position i in both numbers is the same
    if n[i] == num[i]:
        count += 1  # Increment count if digits match
        correct[i] = n[i]  # Store the correct digit in the correct list

print("Number of correct digits:", count)
print("Correct digits:", correct)



# Let's start with a list of numbers
my_list = [1, 2, 3, 4]

# Let's say we want to replace the second element (index 1) with a new value, 5
my_list[1] = 5

# Now, let's print the updated list
print(my_list)
