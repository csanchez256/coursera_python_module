# Lists cannot be multiplied together.

list_a = [1,2,3]
list_b = [2,4,6]

# This throws an error
# list_a * list_b

# To perform element-wise multiplication between two lists, you could
# use a for-loop.
list_c = []
for i in range(len(list_a)):
    list_c.append(list_a[i] * list_b[i])

print(list_c)

# In other words, you cannot do vector muliplication directly, but you can 
# access each elemnt with append(), and multiply them that way.

# NumPy TO THE RESCUE!!! NumPy arrays let you perform array operations.

# Import numpy, aliased as np.
import numpy as np

# Convert lists to arrays.
array_a = np.array(list_a)
array_b = np.array(list_b)

# Perform element-wise multiplication between the arrays.
array_a * array_b

# Arrays cast every element they contain as the same data type.
arr = np.array([1, 2, 'coconut'])
arr

print( type(arr))

arr = np.array([1,2,3])
print (arr.dtype)

# The shape attribute returns the number of elements in each dimension
# of an array.
print(arr.shape)

# Create a 2D array by passing a list of lists to np.array() function.
# Note a 2d matrix is [rows, columns]
arr_2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(arr_2d.shape) # 4 rows, 2 columns
print(arr_2d.ndim)
arr_2d


# Create a 3D array by passing a list of two lists of lists to np.array() function.
arr_3d = np.array([[[1, 2, 3],
                   [3, 4, 5]],

                  [[5, 6, 7],
                   [7, 8, 9]]]
)

print(arr_3d.shape)
print(arr_3d.ndim)
arr_3d

