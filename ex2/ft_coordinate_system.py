#!/usr/bin/env python3

import math


def distance(dest: tuple, src: tuple = (0, 0, 0)) -> str:
    x1, y1, z1 = src
    x2, y2, z2 = dest
    ret = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return f"Distance between {src} and {dest}: {ret:.2f}"


def parsing_coordinates(unchecked_coordinates: str) -> tuple | None:
    try:
        coordinates_list = unchecked_coordinates.split(",")
        if len(coordinates_list) != 3:
            raise ValueError("The number of values ​expected is (3)")
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
    print(distance(pos))
    print()
    coords = "3,4,0"
    print(f"Parsing coordinates: \"{coords}\"")
    pos = parsing_coordinates(coords)
    print(f"Parsed position: {pos}")
    print(distance(pos))
    print()
    coords = "abc,def,ghi"
    print(f"Parsing coordinates: \"{coords}\"")
    parsing_coordinates(coords)
    print()
    (x, y, z) = pos
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
