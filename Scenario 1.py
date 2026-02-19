import numpy as np

marks = np.array([
    [20, 25, 30],
    [22, 28, 26],
    [18, 24, 29]
])
totals = np.sum(marks, axis=0)

top_student = np.argmax(totals)

marks[:, top_student] = marks[:, top_student] * 2

print("Updated Marks After Bonus:\n", marks)
