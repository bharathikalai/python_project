#adding removing and sorting

import numpy as np

arr = np.array([2,1,3,4,5,7,6,8])
#sorting the element
sor = np.sort(arr)
print("the output of sort",sor)

delt = np.delete(arr,7)
print("the value of delt",delt)


delt = np.delete(arr,[1,3])
print("the value of delt",delt)


#concatenate


a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

c = np.concatenate((a,b))
print("the output of concatenate",c)


# #or

z = np.array([[1,2],[3,4]])
y = np.array([[5,6]])

z = np.concatenate((z,y),axis=0)
print("the output of z",z)

#insert

arr = np.array([1,2,3,4,5])
#insert single element at index 2
arra = np.insert(arr,2,80)
print("the output of arr  insert ",arra)

#multiple element

arra = np.insert(arr,3,[7,9])
print("the output of arra the multiple element",arra)



