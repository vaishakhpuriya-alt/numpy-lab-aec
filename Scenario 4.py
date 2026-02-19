import numpy as np

marks = np.array([
    [20, 25, 30],
    [22, 28, 26],
    [18, 24, 29]
])

total = np.sum(marks, axis=0)

max_marks = 3 * 30

percentage = (total / max_marks) * 100

percentage_row = percentage.reshape(1, 3)

print("Student Percentage:\n", percentage_row)
