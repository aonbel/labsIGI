"""
Lab Work 1: Task 2 - Count Negative Numbers
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
"""

def handle_errors(func):
    """Decorator to handle input errors."""
    def wrapper():
        try:
            return func()
        except ValueError:
            print("Invalid input!")
    return wrapper

@handle_errors
def compute() -> int:
    """
    Count negative numbers entered until a number >100 is input.

    Returns:
        int: Count of negative numbers.
    """
    count = 0
    while True:
        num = int(input())
        if num > 100:
            break
        if num < 0:
            count += 1
    return count