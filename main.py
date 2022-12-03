from src.day1.day1 import find_most_calories, find_topmost_calories
from src.day2.rock_paper_scissors import puzzle1_score, puzzle2_score

if __name__ == "__main__":
    print("Solutions:")

    print(f"Day 1, puzzle 1: {find_most_calories()}")
    print(f"Day 1, puzzle 2: {sum(find_topmost_calories(3))}")

    print(f"Day 2, puzzle 1: {puzzle1_score()}")
    print(f"Day 2, puzzle 2: {puzzle2_score()}")
