from dataclasses import dataclass
from pathlib import Path


@dataclass
class Section:
    start: int
    end: int

    @classmethod
    def from_string(cls, string: str) -> "Section":
        """Creates a new section from a string formatted as
        <start>-<end>
        """
        parts = string.split("-")
        return Section(start=int(parts[0]), end=int(parts[1]))

    def contains(self, other: "Section") -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps_with(self, other: "Section") -> bool:
        return (self.end >= other.start and self.end <= other.end) or (
            self.start >= other.start and self.start <= other.end
        )


def __sections_from_pair_string(pair_string: str) -> list[Section, Section]:
    parts = pair_string.split(",")
    return [Section.from_string(parts[0]), Section.from_string(parts[1])]


def __load_pairs_from_file(cleaning_pairs: Path) -> list[Section, Section]:
    with open(cleaning_pairs, "r", encoding="utf-8") as fp:
        pairs = [__sections_from_pair_string(line) for line in fp.readlines()]

    return pairs


def count_overlapping_pairs(
    cleaning_pairs: Path = Path(__file__).parent / "input.txt",
) -> int:
    pairs = __load_pairs_from_file(cleaning_pairs)
    return sum(pair[0].contains(pair[1]) or pair[1].contains(pair[0]) for pair in pairs)


def count_partly_overlapping_pairs(
    cleaning_pairs: Path = Path(__file__).parent / "input.txt",
) -> int:
    pairs = __load_pairs_from_file(cleaning_pairs)

    return sum(
        pair[0].overlaps_with(pair[1]) or pair[1].overlaps_with(pair[0])
        for pair in pairs
    )
