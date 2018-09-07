import numpy as np

#Create array of zeros and ones
#####################################################################
array_of_zeros = np.zeros(shape=(2, 5, 4))
array_of_ones = np.ones(5)

#Create an identity matrix
#####################################################################
print(np.identity(4))

#Find the shape of an array
print("Shape of zero array: " + str(np.shape(array_of_zeros)))
print("Shape of one array: " + str(np.shape(array_of_ones)))

arr = np.array([1, 2, 3, 4])

#Min and max value of arr
#####################################################################
print("Min: " + str(np.min(arr)))
print("Max: " + str(np.max(arr)))

#Returns the INDEX of min and max value of arr
#####################################################################
print("Arg Min: " + str(np.argmin(arr)))
print("Arg Max: " + str(np.argmax(arr)))

#Transpose a matrix
#####################################################################
mat = np.matrix([[1, 2], [3, 4]])
print("Matrix: " + str(mat))
matT = np.transpose(mat)
print("Matrix T: " + str(matT))

#Convert a double matrix to an integer matrix
#####################################################################
floatArr = np.array([1.0, 2.0, 3.0])

integerArr = floatArr.astype(np.int)
integerArr = np.array(floatArr, dtype=np.int)

#Matrix manipulations
#####################################################################
a = np.matrix([[0, 3],[2, 4]])
print("A before: " + str(a))
a += 1
print("A after: " + str(a))

b = np.matrix([[1, 1], [1, 1]])
print("B before: " + str(b))
b[0] = 0
print("B after: " + str(b))

c = np.matrix([[2, 2],[2, 2]])
print("C before: " + str(c))
c[:,0] = 0
print("C after:" + str(c))

#Using Random in NumPy
#####################################################################
normal_samples = np.random.normal(0, 1, 100)
uniform_samples = np.random.uniform(0, 1, 100)

#Sample from an array uniformly
#####################################################################
my_dist = [0.3, 0.2, 0.1, 0.4]
sample_element = np.random.choice(my_dist, size=3)
print(sample_element)
