# Lab Work 4: Task 3
# Version: 1.0
# Developer: Belavusau Anton
# Date: May 10, 2025

from statistics import mean, median, mode, variance, stdev
import numpy as np
import matplotlib.pyplot as plt
import task1_old_lab

def enhance_lab3(data: list):
    """Enhance Lab 3 with statistical calculations and plotting."""
    try:

        stats = {
            'mean': mean(data),
            'median': median(data),
            'mode': mode(data),
            'variance': variance(data),
            'std': stdev(data)
        }

        x = np.linspace(-1, 1, 100)
        y_series = np.array([task1_old_lab.compute(xi, 0.01)[0] for xi in x])
        y_math = np.asin(x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y_series, 'b-', label='Series Approximation')
        plt.plot(x, y_math, 'r--', label='Math Function')
        plt.title('Function Comparison')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.legend()
        plt.savefig('plot.png')
        plt.close()

        return stats
    except Exception as e:
        print(f"Error in Lab 3 enhancement: {e}")
        return {}