def prime_factors(n):
    factors = []  # Initialize an empty list to store prime factors
    for i in range(2, n + 1):  # Iterate through numbers from 2 to n
        while n % i == 0:  # Check if i is a factor of n
            factors.append(i)  # If i is a factor, add it to the list of factors
            n //= i  # Divide n by i repeatedly until it's no longer divisible by i
    return factors  # Return the list of prime factors

# Main function to take user input and print prime factors
def main():
    num = int(input("Enter a number to find its prime factors: "))  # Take user input
    factors = prime_factors(num)  # Find prime factors of the input number
    if len(factors) == 0:  # If no prime factors found
        print("The number itself is prime.")  # Print that the number is prime
    else:
        print("Prime factors of", num, "are:", factors)  # Print the prime factors

if __name__ == "__main__":
    main()  # Call the main function


# x = 4//3
# print(x,"x")

# y = 3 % 2

# print(y,"mod of y")