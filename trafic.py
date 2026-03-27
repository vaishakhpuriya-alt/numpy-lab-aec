import numpy as np

A = np.array([
    [200, 150],
    [100, 250]
])

# 200 represents vehicle go from R1 to R1
# 150 represents vehicle go from R1 to R2
# 100 represents vehicle go from R2 to R1
# 250 represents vehicle go from R2 to R2

T = np.array([
    [0.8, 0.2],
    [0.3, 0.7],
])  # This stimulates new traffic after signal optimisation

A_new = np.dot(A, T)

print("Initial Traffic Matrix:")
print(A)

print("\nTransition Matrix:")
print(T)

print("\nOptimized Traffic Matrix:")
print(A_new)

# Total vehicles per road after optimization
row_sum = np.sum(A_new, axis=1)
print("\nTotal vehicles leaving each road:")
print(row_sum)

# Total vehicles arriving at each road
col_sum = np.sum(A_new, axis=0)
print("\nTotal vehicles arriving at each road:")
print(col_sum)