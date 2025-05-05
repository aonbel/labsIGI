"""
Lab Work 1: Task 5 - List Operations
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
"""

def compute(arr: list[float]) -> tuple[float, float]:
    """
    Compute product of even-indexed elements and sum between first and last zero.

    Args:
        arr (list[float]): Input list.

    Returns:
        tuple[float, float]: 
            - Product of elements at even indices (0, 2, 4...).
            - Sum of elements between first and last zero.

    Raises:
        ValueError: If no zeros or only one zero is found.
    """

    # Calculate product of even indices
    product = 1.0
    for i in range(1, len(arr), 2):
        product *= arr[i]

    # Find first and last zero indices
    try:
        first_zero = arr.index(0)
        last_zero = len(arr) - 1 - arr[::-1].index(0)
    except ValueError:
        raise ValueError("No zeros found in the list")

    if first_zero == last_zero:
        raise ValueError("Only one zero found")

    # Calculate sum between first and last zero
    sum_between = sum(arr[first_zero + 1 : last_zero])

    return (product, sum_between)