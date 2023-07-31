from dataclasses import dataclass
from enum import IntEnum
from typing import NamedTuple


class Clue(NamedTuple):
    sum: int
    length: int


class Direction(IntEnum):
    V = 0
    H = 1


@dataclass(frozen=True)
class WordPos:
    x: int
    y: int
    direction: Direction


# BOARD = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

BOARD = [
    [0, 0],
    [0, 0],

]

# BOARD = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
# ]

# WORD_SUMS_LENGTH = {
#     WordPos(x=0, y=0, direction=Direction.H): Clue(9, 2),
#     WordPos(x=0, y=1, direction=Direction.H): Clue(12, 3),
#     WordPos(x=0, y=2, direction=Direction.H): Clue(14, 3),
#     WordPos(x=0, y=0, direction=Direction.V): Clue(8, 3),
#     WordPos(x=1, y=0, direction=Direction.V): Clue(11, 3),
#     WordPos(x=2, y=1, direction=Direction.V): Clue(16, 2)
# }


WORD_SUMS_LENGTH = {
    WordPos(x=0, y=0, direction=Direction.H): Clue(17, 2),
    WordPos(x=0, y=1, direction=Direction.H): Clue(6, 2),
    WordPos(x=0, y=0, direction=Direction.V): Clue(12, 2),
    WordPos(x=1, y=0, direction=Direction.V): Clue(11, 2)
}

# WORD_SUMS_LENGTH = {
#     WordPos(x=0, y=0, direction=Direction.H): Clue(9, 2),
#     WordPos(x=3, y=0, direction=Direction.H): Clue(17, 2),
#     WordPos(x=0, y=1, direction=Direction.H): Clue(25, 5),
#     WordPos(x=1, y=2, direction=Direction.H): Clue(24, 3),
#     WordPos(x=0, y=3, direction=Direction.H): Clue(15, 5),
#     WordPos(x=0, y=4, direction=Direction.H): Clue(11, 2),
#     WordPos(x=3, y=4, direction=Direction.H): Clue(16, 2),
#     WordPos(x=0, y=0, direction=Direction.V): Clue(16, 2),
#     WordPos(x=0, y=3, direction=Direction.V): Clue(3, 2),
#     WordPos(x=1, y=0, direction=Direction.V): Clue(26, 5),
#     WordPos(x=2, y=1, direction=Direction.V): Clue(10, 3),
#     WordPos(x=3, y=0, direction=Direction.V): Clue(32, 5),
#     WordPos(x=4, y=0, direction=Direction.V): Clue(16, 2),
#     WordPos(x=4, y=3, direction=Direction.V): Clue(14, 2),
#
# }
