n = int(input("enter the number")) # get the input from user

temp = n  #store the user input in temp variable
rev = 0   

while(n>0):
    dig = n%10
    print("dig",dig)
    rev = rev*10+dig
    print("rev",rev)
    n=n//10
    print(n)
if(temp==rev):
    print("the number is a palindrome")
else:
    print("the number isnt a palindrome!")

#second question

class Solution:
    def mergeTwoLists(self, list1,list2):      
        a = sorted(list1 + list2)
        return a


list1 = [1,2,4]
list2 = [1,3,4]
a = Solution()
x = a.mergeTwoLists(list1,list2)
print(x)
