#!/usr/bin/env python3

def list_comprehension() -> None:
    print("=== List Comprehension Examples ===\n")

    scores: list[list[str:int]] = [["alice", 2300, True],
                                   ["bob", 1800, True],
                                   ["charlie", 2150, True],
                                   ["diana", 2050, False]]

    high_scores: list[str] = [score[0] for score in scores if score[1] > 2000]
    print(f"high scores (>2000): {high_scores}")

    doubled_scores: list[int] = [score[1] * 2 for score in scores]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [score[0] for score in scores if score[2] is True]
    print(f"Active players: {active_players}")


def dict_comprehension() -> None:
    player: list[list] = [["alice", 2300, 5], ["bob", 1800, 3], ["charlie", 2150, 7]]
    categories: dict[str:int] = {"high": 3,
                                 "medium": 2,
                                 "low": 1}
    achievement_count: dict[str:int] = {"alice": 5,
                                        "bob": 3,
                                        "charlie": 7}

    print("=== Dict Comprehension Examples ===\n")
    print(f"Player scores: {scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {achievement_count}")


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension()
    print()
    dict_comprehension()


def set_comprehension() -> None:
    players: set[str] = {"alice", "bob", "charlie", "diana", "bob"}

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {players}")
    print(f"Unique achievements: ")

if __name__ == "__main__":
    main()

# === Dict Comprehension Examples ===
# Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
# Score categories: {'high': 3, 'medium': 2, 'low': 1}
# Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}
# === Set Comprehension Examples ===
# Unique players: {'alice', 'bob', 'charlie', 'diana'}
# Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
# Active regions: {'north', 'east', 'central'}
# === Combined Analysis ===
# Total players: 4
# Total unique achievements: 12
# Average score: 2062.5
# Top performer: alice (2300 points, 5 achievements)
