from itertools import permutations, product
from typing import cast, Generator, Optional
from constants import WORD_SUMS_LENGTH, WordPos, Direction


CombinationsType = dict[WordPos, list[tuple[int, ...]]]


def prepare_possible_combinations() -> CombinationsType:
    word_possible_combinations = {}
    for element in WORD_SUMS_LENGTH:
        possible_combinations: list[tuple[int, ...]] = []
        sum_length = WORD_SUMS_LENGTH[element]
        all_combinations = permutations(range(1, 10), sum_length.length)
        for combination in all_combinations:
            if sum(cast(tuple[int, ...], combination)) == sum_length.sum:
                possible_combinations.append(cast(tuple[int, ...], combination))
        word_possible_combinations[element] = possible_combinations
    return word_possible_combinations


def prepare_kakuro_input(combinations_to_try: CombinationsType) -> Generator:
    all_clues = combinations_to_try.values()
    clue_input = product(*all_clues)
    for combination in clue_input:
        board_input = {}
        counter = 0
        for clue in WORD_SUMS_LENGTH:
            board_input[clue] = combination[counter]
            counter += 1
        yield board_input


def fill_in_kakuro(
        combination_input: dict[WordPos, tuple[int, ...]],
        horizontal_board: list[list[int]],
        vertical_board: list[list[int]]
                ) -> Optional[list[list[int]]]:
    for clue in combination_input:
        coordinates = clue
        Y = coordinates.y
        X = coordinates.x
        counter = 0
        for number in combination_input[clue]:
            if coordinates.direction == Direction.H:
                horizontal_board[Y][(X + counter)] = number
                counter += 1
            elif coordinates.direction == Direction.V:
                vertical_board[(Y + counter)][X] = number
                counter += 1
            if horizontal_board == vertical_board:
                return horizontal_board
    return None
