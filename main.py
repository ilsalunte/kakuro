from copy import deepcopy
from tqdm import tqdm
from constants import BOARD
from solution import prepare_possible_combinations, prepare_kakuro_input, fill_in_kakuro


def main() -> None:
    prepared_combinations = prepare_possible_combinations()
    combinations_number = 1
    for combination in prepared_combinations.values():
        combinations_number *= len(combination)
    print(combinations_number)
    prepared_kakuro_input = prepare_kakuro_input(combinations_to_try=prepared_combinations)
    horizontal_board = deepcopy(BOARD)
    vertical_board = deepcopy(BOARD)
    for combination in tqdm(prepared_kakuro_input, total=combinations_number):
        result = fill_in_kakuro(
            combination_input=combination, horizontal_board=horizontal_board, vertical_board=vertical_board
        )
        if result:
            print_result(result=result)
            break


def print_result(result: list[list[int]]) -> None:
    for row in result:
        result_to_print = [str(element) for element in row]
        print(' '.join(result_to_print))


if __name__ == '__main__':
    main()
