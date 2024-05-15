# Mr. Vincent works in a door mat manufacturing company. 
# One day, he designed a new door mat with the following 
#    specifications:


# Mat size must be NXM. ( Nis an odd natural number, and  M is  times N .)
# The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.


# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
# lens = "---------.|.---------"

# print(len(lens))
#method 1

a = int(input())
b = int(a*3)


for x in range(1,((a+1)//2)):
    print((".|."*(x +x -1)).center(b,"-"))


for x in range(1):
    print("WELCOME".center(b,"-"))


for x in range(((a + 1) // 2) - 1, 0, -1):
    print((".|." * (x + x - 1)).center(b, "-"))



# # 1
# # 2
# 3



# (4  +1) - 1 -1

# (4 + 2) - 2 - 1





# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------


#method two

def mat_design(height: int, length: int) -> None:
    pattern = '.|.'
    message = 'WELCOME'
    
    if height % 2 == 0 or length != 3 * height:
        return

    # PATTERN PRINTING #
    for i in range(height // 2):
        print(f'{(1 + (i * 2)) * pattern:-^{length}}')
    print(f'{message:-^{length}}')
    for i in range(height // 2, 0, -1):
        print(f'{((i * 2) - 1) * pattern:-^{length}}')



input_data = input().split() 


mat_design(*map(int, input_data))




