import numpy as np

# Create 3x3 array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original 3x3 Array:")
print(arr)

# Reshape to (1,9)
reshaped_arr = arr.reshape(1, 9)

print("\nReshaped Array (1x9):")
print(reshaped_arr)
