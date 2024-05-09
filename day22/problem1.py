#Print each subsequence on a new line. There will be  of them. No return value is expected.

# Input Format

# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.

# sample input 

# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3



# Sample Output

# AB
# CA
# AD


# aab
# caa
# ada
#i want  like aab   caa   ada

#method 1

def merge_the_tools(string, k):
    leng = len(string)

    for x in range(0,leng,k):
        a = string[x:x+k]
        uniqe = set(a)
        new_string = ''.join(uniqe)
        print(new_string)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


