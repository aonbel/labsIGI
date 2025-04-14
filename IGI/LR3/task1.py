"""
Lab Work 1: Task 1 - Series Computation
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
"""

def compute(x: float, eps: float) -> tuple[float, int]:
    """
    Compute the series sum until the term is less than epsilon.

    Args:
        x (float): Input value.
        eps (float): Precision threshold.

    Returns:
        tuple[float, int]: Result and number of iterations.
    """
    numerator = 1
    denominator = 1
    pow_x = x
    result = 0.0
    needed_iter = 0
    for iter in range(500):
        curr = numerator / ((2 * iter + 1) * denominator) * pow_x
        if abs(curr) < eps:
            needed_iter = iter
            break
        result += curr
        numerator *= (2 * iter + 1) * (2 * iter + 2)
        denominator *= 4 * (iter + 1) ** 2
        pow_x *= x * x
    return (result, needed_iter)