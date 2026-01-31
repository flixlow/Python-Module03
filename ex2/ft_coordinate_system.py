#!/usr/bin/env python3

import math


def distance(src: tuple = (0, 0, 0), dest: tuple = (0, 0, 0)) -> None:
    x1, y1, z1 = src
    x2, y2, z2 = dest
    ret = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    print(f"Distance between {dest} and {src}: {ret:.2f}")


def parsing_coordinates(unchecked_coordinates: str) -> tuple:
    try:
        coordinates_list = unchecked_coordinates.split(",")
        x = int(coordinates_list[0])
        y = int(coordinates_list[1])
        z = int(coordinates_list[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e}")
    else:
        return (x, y, z)


def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    print()
    pos = parsing_coordinates("10,20,5")
    print(f"Position created: {pos}")
    distance(pos)
    print()
    coords = "3,4,0"
    print(f"Parsing coordinates: \"{coords}\"")
    pos = parsing_coordinates(coords)
    print(f"Parsed position: {pos}")
    distance(pos)
    print()
    coords = "abc,def,ghi"
    print(f"Parsing coordinates: \"{coords}\"")
    print()
    (x, y, z) = pos
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()

# === Game Coordinate System ===
# Position : (10, 20, 5)
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
