from src.day4.camp_cleanup import (
    count_overlapping_pairs,
    count_partly_overlapping_pairs,
)
from . import TEST_RESOURCES


def test_overlapping_pairs_count():
    assert count_overlapping_pairs(TEST_RESOURCES / "day4_example.txt") == 2


def test_partly_overlapping_pairs_count():
    assert count_partly_overlapping_pairs(TEST_RESOURCES / "day4_example.txt") == 4
