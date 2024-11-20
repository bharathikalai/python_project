#size 3  >> inout
#  >> output


# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------








# size = 26
#     # your code goes here
# alphabet = "abcdefghijklmnopqrstuvwxyz"


# my_list = []
    
# for i in range(size):
#         s = "-".join(alphabet[size - 1 : size - 1 - i : -1] + alphabet[size - i - 1: size])

#         my_list.append(s.center(4 * size - 3, "-"))
    
# print("\n".join(my_list + my_list[-2::-1]))
        



# a =  [10, 20, 30, 40, 50]

# result = a[-2::-4]
# print("result",result)


# a = "abcdefgh"

# result = a[2:-7:1]
# print(result)


# the input is 3


# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


# alp = "1234"

# result = alp[3:2:-3]

# print(result,"the value of result")




# --------------------------------------------------z--------------------------------------------------
# ------------------------------------------------z-y-z------------------------------------------------
# ----------------------------------------------z-y-x-y-z----------------------------------------------
# --------------------------------------------z-y-x-w-x-y-z--------------------------------------------
# ------------------------------------------z-y-x-w-v-w-x-y-z------------------------------------------
# ----------------------------------------z-y-x-w-v-u-v-w-x-y-z----------------------------------------
# --------------------------------------z-y-x-w-v-u-t-u-v-w-x-y-z--------------------------------------
# ------------------------------------z-y-x-w-v-u-t-s-t-u-v-w-x-y-z------------------------------------
# ----------------------------------z-y-x-w-v-u-t-s-r-s-t-u-v-w-x-y-z----------------------------------
# --------------------------------z-y-x-w-v-u-t-s-r-q-r-s-t-u-v-w-x-y-z--------------------------------
# ------------------------------z-y-x-w-v-u-t-s-r-q-p-q-r-s-t-u-v-w-x-y-z------------------------------
# ----------------------------z-y-x-w-v-u-t-s-r-q-p-o-p-q-r-s-t-u-v-w-x-y-z----------------------------
# --------------------------z-y-x-w-v-u-t-s-r-q-p-o-n-o-p-q-r-s-t-u-v-w-x-y-z--------------------------
# ------------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-n-o-p-q-r-s-t-u-v-w-x-y-z------------------------
# ----------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----------------------
# --------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--------------------
# ------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z------------------
# ----------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----------------
# --------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--------------
# ------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z------------
# ----------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----------
# --------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--------
# ------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z------
# ----z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----
# --z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--
# z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z
# --z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--
# ----z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----
# ------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z------
# --------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--------
# ----------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----------
# ------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z------------
# --------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--------------
# ----------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----------------
# ------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z------------------
# --------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z--------------------
# ----------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z----------------------
# ------------------------z-y-x-w-v-u-t-s-r-q-p-o-n-m-n-o-p-q-r-s-t-u-v-w-x-y-z------------------------
# --------------------------z-y-x-w-v-u-t-s-r-q-p-o-n-o-p-q-r-s-t-u-v-w-x-y-z--------------------------
# ----------------------------z-y-x-w-v-u-t-s-r-q-p-o-p-q-r-s-t-u-v-w-x-y-z----------------------------
# ------------------------------z-y-x-w-v-u-t-s-r-q-p-q-r-s-t-u-v-w-x-y-z------------------------------
# --------------------------------z-y-x-w-v-u-t-s-r-q-r-s-t-u-v-w-x-y-z--------------------------------
# ----------------------------------z-y-x-w-v-u-t-s-r-s-t-u-v-w-x-y-z----------------------------------
# ------------------------------------z-y-x-w-v-u-t-s-t-u-v-w-x-y-z------------------------------------
# --------------------------------------z-y-x-w-v-u-t-u-v-w-x-y-z--------------------------------------
# ----------------------------------------z-y-x-w-v-u-v-w-x-y-z----------------------------------------
# ------------------------------------------z-y-x-w-v-w-x-y-z------------------------------------------
# --------------------------------------------z-y-x-w-x-y-z--------------------------------------------
# ----------------------------------------------z-y-x-y-z----------------------------------------------
# ------------------------------------------------z-y-z------------------------------------------------
# --------------------------------------------------z--------------------------------------------------






# from collections import Counter


# aa = list(input())


# bb = Counter(aa)

# print(bb)


# no_customer = list(input(int()))

# shoe_size = 


# s = set('HackerRank')
# s.add('B')

# print("s",s)


# country_name = input().strip()

# no_of_county = len(country_name.split())

# total_county = set(country_name)

# def outputing(country_name):

#     change_set = set(country_name)

#     return change_set

# num_of_county = int(input())

# country_name = input().strip()

# result = outputing(country_name)

# print(result)



# user_input = int(input())

# countries_stamps = set()

# for i in range(user_input): 
#     country = input().strip() 
#     countries_stamps.add(country)

# print(len(countries_stamps))



# import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

# userinput_month = int(input("enter the month"))
# userinput_day = int(input("enter the day"))
# userinput_year = int(input("enter the year"))

# print(calendar.day_name[calendar.weekday(userinput_year, userinput_month,userinput_day)]) 


# import calendar

# userinput_year, userinput_month , userinput_day = list(map(int,input().strip()))

# print(calendar.day_name[calendar.weekday(userinput_year, userinput_month,userinput_day)]) 


s = ['1', '2', '3', '4']
res = map(float, s)
print(list(res))