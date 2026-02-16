import numpy as np

# Create two 2x2 matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
result = np.dot(A, B)
# You can also use: result = A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication Result:")
print(result)
