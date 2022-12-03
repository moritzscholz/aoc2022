from src.day3.find_items import Item, sum_of_item_priorities
from . import TEST_RESOURCES


def test_priorities():
    assert Item("a").priority == 1
    assert Item("c").priority == 3
    assert Item("z").priority == 26
    assert Item("A").priority == 27
    assert Item("C").priority == 29
    assert Item("Z").priority == 52


def test_example():
    assert sum_of_item_priorities(TEST_RESOURCES / "day3_example.txt") == 157
