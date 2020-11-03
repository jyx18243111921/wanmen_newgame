import numpy as np
vector = np.array([5,10,15])
matrix = np.array([[5,10,15],[20,25,30],[35,40,45],[5,10,15],[20,25,30],[35,40,45]])
equal_to_ten = vector ==10
print(equal_to_ten)
print(vector[equal_to_ten])
second_colum_25 = (matrix[:,1]) == 25
print(matrix[second_colum_25,: 66])
print(help(np.array))
print(vector.dtype)
a = matrix.sum(axis=1)
print(a)

print(np.arange(15))
b = np.arange(8).reshape(2,2,2)
print(b)
