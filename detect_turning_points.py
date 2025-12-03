import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    if not isinstance(signal, np.ndarray):
        return None
    if signal.ndim != 1:
        return None
    if signal.size < 3:
        turning_indices = np.array([], dtype=int)
        x = np.arange(signal.size)
        plt.figure()
        plt.plot(x, signal, marker="o")
        plt.xlabel("Index")
        plt.ylabel("Signal")
        plt.title("Signal with Turning Points")
        plt.savefig(filename, format="pdf")
        plt.close()
        return turning_indices

    diffs = np.diff(signal)

    signs = np.sign(diffs)

    turning_indices = []
    for i in range(len(signs) - 1):
        if signs[i] * signs[i + 1] < 0:
            turning_indices.append(i + 1)

    turning_indices = np.array(turning_indices, dtype=int)

    x = np.arange(signal.size)

    plt.figure()
    plt.plot(x, signal, marker="o", linestyle="-", label="Signal")

    if turning_indices.size > 0:
        plt.scatter(
            turning_indices,
            signal[turning_indices],
            marker="o",
            s=80,
            label="Turning points"
        )

    plt.xlabel("Index")
    plt.ylabel("Signal")
    plt.title("Signal with Turning Points")
    plt.legend()

    plt.savefig(filename, format="pdf")
    plt.close()

    return turning_indices