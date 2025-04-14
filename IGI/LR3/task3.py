"""
Lab Work 1: Task 3 - Binary String Check
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
"""

def compute(s: str) -> bool:
    """
    Check if a string consists only of '0' and '1'.

    Args:
        s (str): Input string.

    Returns:
        bool: True if binary, False otherwise.
    """
    for char in s:
        if char not in {'0', '1'}:
            return False
    return True