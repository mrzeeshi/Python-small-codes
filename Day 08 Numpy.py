# Today in this python file we will play with the numpy library.
# The numpy is the famous python library that is used to perform the numerical operations on the heavy amount of the data.
# We use the numpy because the lists when large amount of data is stored in them become too slow
# This is the basic practice file in which we will try to make the arrays using the numpy

import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)

#Now if we want to make an array of any size which has only zeros
zero_array=np.zeros((3,3))
print("The 3x3 array having only zeroes... \n",zero_array)


#Now we will make the array that has only ones....
print("The 2x3 array with only having the ones...\n",np.ones((2,3)))

#Now we will try to make the array with a range and constant increment on each value...
print()
print("The array from 0 to 10 with 2 incremet on each element...\n ", np.arange(0,10,2))

#Now the array of any size having the diagonal as 1s
print()
print("The array of size 3x3 having diagonal as one...\n",np.eye(3))

#Now we will try to make an array of n equal steps...
print()
print("An array of 5 equal steps...\n",np.linspace(0,10,5))

#Now finding the dimensions of an array...
print("\n The array having the dimensions...\n ",zero_array,"\n Dimensions: ",zero_array.shape)

#Now giving the size of an array.....
print(f"\nThe size of \n{zero_array} is {zero_array.size}")

#Now we will try to change the shape of an array
print(f"\n Array Before: \n{arr}\n Array After: \n {arr.reshape(2,3)}")