n = int(input("enter the input"))  #get the user input 5

temp = n   

rev = 0     #set rev varibale 0

while(n>0):    #loop started  if the n greaterthan 0 then only this loop will exicute
    dig = n%10      # if the n is 5 this dig value will be 5 because we are using modules %  
    rev = rev*10+n  #first itteration this rev value will be  5 
    n=n//10    #  n value is 5 i am divide 5 with 10 answer will be 0.5 we are using // which mean it will remove .5 this value
if(temp == rev):  #n value is 0 so second itteration will do exicute  here checking the value in rev i got 5 my temp value is also 5 so if condition is true
    print("the number is palindrome"
          )
else:
    print("the number is not palindrome")




class Solution:
    def isPalindrome(self, x):
        rev = 0
        temp = x
        while(x >0):
            dig = x % 10
            rev = rev*10+dig
            x=x//10
        if(temp==x):
            return True
        else:
            False


x = Solution()

y = x.isPalindrome(121)
print(y)