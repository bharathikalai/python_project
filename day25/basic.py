#python basics

import numpy as np

arr = np.array([1,2,3,4,5])

print("Array", arr)

result_sum = np.sum(arr)
result_mean = np.mean(arr)
result_max = np.max(arr)
result_min = np.min(arr)


print("result_sum",result_sum)
print("result_mean",result_mean)
print("result_max",result_max)
print("result_min",result_min)


#how to create basic array

a = np.array([1,2,3,4,5,6])
print("the basic array",a)


# you can easily create an array filled with 0’s

a = np.zeros(10)
print("the value of a",a)


# you can easily create an array filled with 1’s
b = np.ones(100)
print("the value of b",b)


# Or even an empty array! The function empty creates an array whose initial content is random and depends on the state of the memory. 


b = np.empty(20)
print("the value of b",b)



#range

c = np.arange(10)
print("the value of c  this is range",c)



#linespace

b = np.linspace(0,10, num=4)

print("the of b line space",b)



#specfiy tour data type


b = np.ones(2, dtype=np.float64)
print("the value of b spefiy the data type",b)