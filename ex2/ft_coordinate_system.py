#!/usr/bin/env python3

import sys
import math


def distance(pos: tuple) -> None:
    x, y, z = pos
    ret = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between (0, 0, 0) and {pos}: {ret:.2f}")


def check_coordinates() -> tuple:
    try:
        x = type(sys.argv[1])
        y = type(sys.argv[2])
        z = type(sys.argv[3])
    except ValueError:
        raise ValueError()
    return (x, y, z)


def ft_coordinate_system():
    try:
        pos = check_coordinates()
    except ValueError as e:
        print(f"Error details - Type: ValueError, Args: ({e})")
    print(f"Position created: {pos}")
    distance(pos)


def main():
    print("=== Game Coordinate System ===")
    ft_coordinate_system()


if __name__ == "__main__":
    main()

# === Game Coordinate System ===
# Position created: (10, 20, 5)
# Distance between (0, 0, 0) and (10, 20, 5): 22.91

# Parsing coordinates: "3,4,0"
# Parsed position: (3, 4, 0)
# Distance between (0, 0, 0) and (3, 4, 0): 5.0

# Parsing invalid coordinates: "abc,def,ghi"
# Error parsing coordinates: invalid literal for int() with base 10: 'abc'
# Error details - Type: ValueError, Args: ("invalid literal for int() with
# base 10: 'abc'",)

# Unpacking demonstration:
# Player at x=3, y=4, z=0
# Coordinates: X=3, Y=4, Z=0
