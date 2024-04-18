
def unique_substring(s):
    unique = set()
    n = len(s)

    for i in range(n):
        for j in range(i+1,n+1):
            unique.add(s[i:j])
    return len(unique)




input_string = "abc"
print("Number of unique substring",unique_substring(input_string))