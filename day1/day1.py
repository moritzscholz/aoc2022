from pathlib import Path


def find_most_calories() -> int:
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r", encoding="utf-8") as fp:
        blocks = fp.read().split("\n\n")

    total_calories = [sum(int(c) for c in b.strip().split("\n")) for b in blocks]

    return max(total_calories)
