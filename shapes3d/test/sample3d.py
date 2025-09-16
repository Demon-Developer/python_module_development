import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shapes3d import (
    area_of_cube,
    area_of_cuboid,
    area_of_cylinder,
    area_of_cone,
    area_of_sphere
)

def main():
    print("Surface Area of Cube (side=5):", area_of_cube(5))
    print("Surface Area of Cuboid (l=4, b=3, h=2):", area_of_cuboid(4, 3, 2))
    print("Surface Area of Cylinder (r=3, h=7):", area_of_cylinder(3, 7))
    print("Surface Area of Cone (r=4, slant=6):", area_of_cone(4, 6))
    print("Surface Area of Sphere (r=5):", area_of_sphere(5))

if __name__ == "__main__":
    main()
