import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print("Original 3x2 Matrix A:")
print(A)

A_transpose = A.T

print("\nTranspose of A (2x3):")
print(A_transpose)

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("\nMatrix B (3x2):")
print(B)

result = np.dot(A_transpose, B)

print("\nDot Product Result:")
print(result)

