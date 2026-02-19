import numpy as np

marks = np.array([
    [20, 25, 30],
    [22, 28, 26],
    [18, 24, 29]
])

average = np.mean(marks, axis=1)

average_column = average.reshape(3, 1)

print("Average Marks per Subject:\n", average_column)
