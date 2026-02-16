import numpy as np

# Create two 2D arrays
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [1, 2, 3]])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

# Element-wise multiplication
result = arr1 * arr2

print("\nElement-wise Multiplication Result:")
print(result)
