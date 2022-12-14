from src.day1.day1 import find_most_calories, find_topmost_calories
from src.day2.rock_paper_scissors import puzzle1_score, puzzle2_score
from src.day3.find_items import sum_of_item_priorities, sum_of_badge_priorities
from src.day4.camp_cleanup import (
    count_overlapping_pairs,
    count_partly_overlapping_pairs,
)

if __name__ == "__main__":
    print("Solutions:")

    print(f"Day 1, puzzle 1: {find_most_calories()}")
    print(f"Day 1, puzzle 2: {sum(find_topmost_calories(3))}")

    print(f"Day 2, puzzle 1: {puzzle1_score()}")
    print(f"Day 2, puzzle 2: {puzzle2_score()}")

    print(f"Day 3, puzzle 1: {sum_of_item_priorities()}")
    print(f"Day 3, puzzle 2: {sum_of_badge_priorities()}")

    print(f"Day 4, puzzle 1: {count_overlapping_pairs()}")
    print(f"Day 4, puzzle 2: {count_partly_overlapping_pairs()}")
