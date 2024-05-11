# Given an integer,n , print the following values for each integer i from 1 to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary



# def print_formatted(number):

#     bin_str = bin(number)[2:]
#     bin_len = len(bin_str)
#     for x in range(1,number+1):
#         decimal = str(x).rjust(bin_len)
#         oct = oct(x)[2:].rjust(bin_len)
#         print(oct)

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)



   
def print_formatted(number):
    # your code goes here
    if 1 <= number <= 99:

        binary_str = bin(number)[2:]
        binary_len = len(binary_str) # binary representation length

        for i in range(1, number+1):
            decimal = str(i).rjust(binary_len)
            octal = oct(i)[2:].rjust(binary_len)
            hexadecimal = hex(i).upper()[2:].rjust(binary_len)
            binary = bin(i)[2:].rjust(binary_len)
            print(decimal, octal, hexadecimal, binary)

        return 


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)