# Lab Work 4: Task 5
# Version: 1.0
# Developer: Belavusau Anton
# Date: May 10, 2025

import numpy as np

def matrix_operations(n: int, m: int):
    """Perform matrix operations for variant 2."""
    try:
        A = np.random.randint(0, 100, size=(n, m))
        print("Matrix A:\n", A)

        mean_A = np.mean(A)
        greater_than_mean = A[A > mean_A]
        count = greater_than_mean.size
        mean_greater = np.mean(greater_than_mean)

        std_numpy = np.std(greater_than_mean)

        squared_diff = [(x - mean_greater) ** 2 for x in greater_than_mean]
        std_manual = np.sqrt(sum(squared_diff) / len(squared_diff))

        return {
            'count': count,
            'std_numpy': round(std_numpy, 2),
            'std_manual': round(std_manual, 2)
        }
    except Exception as e:
        print(f"Error in matrix operations: {e}")
        return {}