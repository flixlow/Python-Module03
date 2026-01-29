#!/usr/bin/env python3

import sys

class Missing(ValueError):
    pass


class Banana(ValueError):
    pass


def ft_score_analytics() -> str:
    output = []
    scores = []
    output.append("=== Player Score Analytics ===")
    for score in sys.argv[1:]:
        scores.append(int(score))
    argc = len(scores)
    if argc == 0:
        output.append("No scores provided. Usage: python3\
 ft_score_analytics.py <score1> <score2> ...")
        raise Missing("\n".join(output))
    for score in scores:
        if type(int(score)) is not int:
            output.append(f"{score} is not type int.")
            raise Banana("\n".join(output))

    output.append(f"Scores processed: {scores}")
    output.append(f"Total players: {argc - 1}")
    # total = sum(scores)
    # output.append(f"Total score: {total}")
    # output.append(f"Average score: {total // argc}")
    # maxi = max(scores)
    # output.append(f"High score: {maxi}")
    # mini = min(scores)
    # output.append(f"Low score: {mini}")
    # output.append(f"Score range: {maxi - mini}")
    return "\n".join(output)


def main() -> None:
    try:
        print(ft_score_analytics())
    except (Missing, Banana) as e:
        print(e)


if __name__ == "__main__":
    main()
