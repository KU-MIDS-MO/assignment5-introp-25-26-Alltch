import numpy as np
import matplotlib.pyplot as plt

# Write a function `column_range_plot(A, filename="column_ranges.pdf")` that;

# - receives a 2D NumPy array `A`,
# - computes the range (maximum minus minimum) of each column,
# - create a bar plot showing the ranges of all columns,
# - saves the plot as a PDF file,
# - and returns a 1D NumPy array containiing the column ranges.


def column_range_plot(A, filename="column_ranges.pdf"):
    if not isinstance(A, np.ndarray):
        return None
    if A.ndim != 2:
        return None
    
    col_max = np.max(A, axis=0)
    col_min = np.min(A, axis=0)
    ranges = col_max - col_min

    plt.figure()
    plt.bar(np.arange(len(ranges)), ranges)
    plt.xlabel("Column index")
    plt.ylabel("Range (max - min)")
    plt.title("Column Ranges")

    plt.savefig(filename, format="pdf")
    plt.close()

    return ranges

A = np.array([
    [1., 4., 9.],
    [3., 1., 5.],
    [7., 2., 8.]
    ])

column_range_plot(A)
