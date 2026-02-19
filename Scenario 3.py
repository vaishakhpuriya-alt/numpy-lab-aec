import numpy as np

marks = np.array([
    [15, 25, 30],
    [18, 28, 26],
    [12, 24, 29]
])

marks[marks < 20] = 20

flattened = marks.flatten()

print("Updated Marks:\n", marks)
print("Flattened Format:\n", flattened)
