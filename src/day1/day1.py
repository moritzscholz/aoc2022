from pathlib import Path


def __list_of_calories() -> list[int]:
    """Reads the input file into blocks of calories in the elve's backpack"""
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r", encoding="utf-8") as fp:
        blocks = fp.read().split("\n\n")

    total_calories = [sum(int(c) for c in b.strip().split("\n")) for b in blocks]

    return total_calories


def find_most_calories() -> int:
    """Finds the most calories in the input list."""
    total_calories = __list_of_calories()

    return max(total_calories)


def find_topmost_calories(items: int) -> list[int]:
    """Finds the topmost `items` calories."""
    top_calories: list(int) = []
    total_calories = __list_of_calories()

    for _ in range(0, items):
        (idx, calories) = max(enumerate(total_calories), key=lambda v: v[1])
        total_calories[idx] = 0
        top_calories += [calories]

    return top_calories
