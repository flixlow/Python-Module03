#!/usr/bin/env python3

import sys


def ft_score_analytics() -> str:
    output = []
    scores: list = []
    output.append("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc == 1:
        output.append("No scores provided. Usage: python3\
 ft_score_analytics.py <score1> <score2> ...")
        return "\n".join(output)
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            output.append(f"oops, {score} is not type int!")
            return "\n".join(output)
    output.append(f"Scores processed: {scores}")
    output.append(f"Total players: {argc - 1}")
    total = sum(scores)
    output.append(f"Total score: {total}")
    output.append(f"Average score: {total / (argc - 1)}")
    maxi = max(scores)
    output.append(f"High score: {maxi}")
    mini = min(scores)
    output.append(f"Low score: {mini}")
    output.append(f"Score range: {maxi - mini}")
    return "\n".join(output)


def main() -> None:
    print(ft_score_analytics())


if __name__ == "__main__":
    main()
