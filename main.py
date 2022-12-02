from day1.day1 import find_most_calories, find_topmost_calories

if __name__ == "__main__":
    print("Solutions:")

    print(f"Day 1, puzzle 1: {find_most_calories()}")
    print(f"Day 1, puzzle 2: {sum(find_topmost_calories(3))}")
