#!/usr/bin/env python3

def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    print()
    a: set = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    b: set = {"first_kill", "level_10", "boss_slayer", "collector"}
    c: set = {"level_10", "treasure_hunter", "boss_slayer"}
    c.add("speed_demon")
    c.add("perfectionist")
    print(f"Player alice achievements: {a}")
    print(f"Player bob achievements: {b}")
    print(f"Player charlie achievements: {c}")
    print()
    print("=== Achievement Analytics ===")
    print()
    union = a.union(b, c)
    print(f"All unique achievements: {a | b | c}")
    print(f"Total unique achievements: {len(union)}")
    print()
    print(f"Common to all players: {a.intersection(b, c)}")
    print(f"Rare achievements: {union - ((a & b) | (a & c) | (b & c))}")
    print()
    print(f"Alice vs Bob common: {a & b}")
    print(f"Alice unique: {a - b}")
    print(f"Bob unique: {b - a}")


if __name__ == "__main__":
    ft_achievement_tracker()
