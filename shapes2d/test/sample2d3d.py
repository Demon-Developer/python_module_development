import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shapes2d.shapes_area import (
    area_of_circle,
    area_of_parallelogram,
    area_of_rectangle,
    area_of_square,
    area_of_trapezoid,
    area_of_triangle,
)

def main():
    #for 2d shapes
    print("Area of Circle (r=5):", area_of_circle(5))
    print("Area of Parallelogram (b=10, h=6):", area_of_parallelogram(10, 6))
    print("Area of Rectangle (l=8, b=4):", area_of_rectangle(8, 4))
    print("Area of Square (side=7):", area_of_square(7))
    print("Area of Trapezoid (b1=6, b2=10, h=5):", area_of_trapezoid(6, 10, 5))
    print("Area of Triangle (b=12, h=6):", area_of_triangle(12, 6))

if __name__ == "__main__":
    main()
