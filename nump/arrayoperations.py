from numpy import *

#copying an array

arr1 = array([1,2,3,4,5,6])


arr4 = arr1.view()  # shallow copy of an array meaning the arrays are dependent on each other and values changed in
                    # one array is change in the other array
arr5 = arr1.copy()  # deep copy of an array
arr1[1] = 7
print(arr4)
print(arr1)
print(arr5)
print(id(arr1))
print(id(arr4))


#
# # adding to arrays
# arr1 = array([1,2,3,4,5,6])
# arr2 = array([4,5,6,7,8,9])
#
# arr3 = arr1 + arr2
# print(arr3)
#
#
# # adding value to each element in an array
#
# arr1 = array([1,2,3,4,5,6])
#
# arr1 = arr1 + 5
#
# print(arr1)
#
#
# # trigonometric operations on an array
#
# arr1 = array([1,2,3,4,5,6])
# print(sin(arr1))
# print(cos(arr1))
# print(tan(arr1))
# print(log(arr1))  # log of an array
# print(sqrt(arr1))  # square root of an array
# print(sum(arr1))
# print(min(arr1))
# print(sort(arr1))
#
# print(concatenate([arr1, arr2]))

