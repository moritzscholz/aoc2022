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

        return cls(content)

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
