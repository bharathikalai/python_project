#how do you know the shape and size of an array?
import numpy as np

array_example = np.array([[[0,1,2,3],[4,5,6,7]],[[0,1,2,3],[4,5,6,7]],[[9,2,1,99],[8,9,9,0]]])

print("the value of array_example",array_example)

print("find the arry dim ",array_example.ndim)

#size

print("find the size of the array",array_example.size)


#shape

print("find the shape of the array",array_example.shape)




#can you reshape the array

