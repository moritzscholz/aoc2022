from pathlib import Path
from dataclasses import dataclass
import logging

ORD_OFFSET_LOWERCASE = -97 + 1
ORD_OFFSET_UPPERCASE = -65 + 27


@dataclass
class Item:
    character: str

    @property
    def priority(self) -> int:
        return ord(self.character) + (
            ORD_OFFSET_LOWERCASE if self.character.islower() else ORD_OFFSET_UPPERCASE
        )

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Item):
            return self.character == __o.character

        return False


@dataclass
class Rucksack:
    content: list[list[Item]]

    @classmethod
    def from_string(cls, content_string: str) -> "Rucksack":
        first_compartment = content_string[: len(content_string) // 2]
        second_compartment = content_string[len(content_string) // 2 :]

        content = [
            cls.__items_from_string(first_compartment),
            cls.__items_from_string(second_compartment),
        ]

        return Rucksack(content)

    @staticmethod
    def __items_from_string(string: str) -> list[Item]:
        return [Item(c) for c in string]

    def item_in_both_compartments(self) -> Item:
        for item1 in self.content[0]:
            if item1 in self.content[1]:
                return item1

        raise ValueError(
            "There is no item in both compartments. Rucksack content is: "
            + self.content
        )

    @property
    def items(self) -> list[Item]:
        return [item for compartment in self.content for item in compartment]

    def contains(self, item: Item) -> bool:
        return item in self.items


@dataclass
class Group:
    rucksacks: list[Rucksack]

    @classmethod
    def from_rows(cls, rows: list[str]) -> "Group":
        return Group(rucksacks=[Rucksack.from_string(row) for row in rows])

    @property
    def badge(self) -> Item:
        for item in self.rucksacks[0].items:
            if all(r.contains(item) for r in self.rucksacks[1:]):
                return item

        raise ValueError("There is no item that is contained in all rucksacks.")


def __find_items_in_both_compartments(packing_info: Path) -> list[Item]:
    with open(packing_info, "r", encoding="utf-8") as fp:
        rucksacks: list[Rucksack] = [Rucksack.from_string(s) for s in fp.readlines()]

    logging.debug("%s rucksacks", len(rucksacks))

    return [r.item_in_both_compartments() for r in rucksacks]


def sum_of_item_priorities(
    packing_info: Path = Path(__file__).parent / "input.txt",
) -> int:
    return sum(
        item.priority for item in __find_items_in_both_compartments(packing_info)
    )


def sum_of_badge_priorities(
    packing_info: Path = Path(__file__).parent / "input.txt", group_size: int = 3
) -> int:
    groups: list[Group] = []

    with open(packing_info, "r", encoding="utf-8") as fp:
        while True:
            rows: list[str] = [fp.readline() for _ in range(0, group_size)]
            if len(rows[-1].strip()) == 0:
                break
            groups.append(Group.from_rows(rows))

    return sum(g.badge.priority for g in groups)
