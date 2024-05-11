#hacker rank question



# You are given a string N .
# Your task is to verify that N is a floating point number.

# In this task, a valid float number must satisfy all of the following requirements:

# number can start with +,- or .symbol


# for exmaple

# +4.50
# ✔
# -1.0
# ✔
# .5
# ✔
# -.7
# ✔
# +.4
# ✖
#  -+4.5


def find_the_flot(a):
    if a in "+":
        return True
    elif a in "-":
        return True
    elif a in ".":
        return True
    elif a in "-.":
        return True
    elif a in "+.":
        return True

    else:
        return False







b = int(input())

find_the_flot(b)

