import os
import sys
from geometric_lib import circle, square

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <shape> <params>")
        return

    shape = sys.argv[1].lower()
    params = list(map(float, sys.argv[2:]))

    if shape == "circle" and len(params) == 1:
        radius = params[0]
        print(f"Circle area: {circle.area(radius)}")
    elif shape == "square" and len(params) == 1:
        a = params[0]
        print(f"Square area: {square.area(a)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
