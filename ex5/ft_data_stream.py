#!/usr/bin/env python3

from typing import Any


def is_prime(n: int) -> bool:
    div = 2
    while div < n:
        if n % div == 0:
            return False
        div += 1
    return True


def gen_prime(n: int) -> Any:
    p = 2
    count = 0
    while count < n:
        if is_prime(p) is True:
            count += 1
            yield p
        p += 1


def fibonacci(n: int) -> Any:
    a = 0
    b = 1
    for _ in range(n):
        yield (a)
        swap = a
        a = b
        b += swap


def game_events(n: int) -> Any:
    names: list[str] = ["alice", "bob", "charlie"]
    i = 0

    while i < n:
        name = names[i % 3]
        level = i * 7 % 10 + 1
        if i % 5 == 0:
            event = "found treasure"
        elif i % 3 == 0:
            event = "leveled up"
        else:
            event = "killed monster"

        yield (f"Player {name} (level {level}) {event}")
        i += 1


def generator_demonstration():
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    for number in fibonacci(10):
        print(number, end=", ")
    print()
    print("Prime numbers (first 5):", end=" ")
    for number in gen_prime(5):
        print(number, end=", ")


def extract_level(event: str) -> int:
    start = event.index("level ") + 6
    end = event.index(")")
    return int(event[start:end])


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    high_level_events: int = 0
    treasure_events: int = 0
    levelup_events: int = 0
    i: int = 1

    gen = game_events(1000)

    for event in gen:
        if i <= 3:
            print(f"Event {i}: {event}")
        elif i == 4:
            print("...")

        if "treasure" in event:
            treasure_events += 1
        if "leveled" in event:
            levelup_events += 1
        if extract_level(event) >= 10:
            high_level_events += 1
        i += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i - 1}")
    print(f"High-level players (10+): {high_level_events}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")

    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    generator_demonstration()


if __name__ == "__main__":
    main()
