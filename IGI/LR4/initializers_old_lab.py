"""
Lab Work 1: Data Initializers
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
"""

def initialize_list_generator(n: int):
    """Generate a list using a simple generator."""
    for iter in range(n-1):
        yield float(iter) / 2

    yield 0

def initialize_list_input() -> list[float]:
    """Read a list from user input."""
    return list(map(float, input("Enter numbers: ").split()))