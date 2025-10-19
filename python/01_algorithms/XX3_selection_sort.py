from math import inf
from typing import List


def selection_sort_v1(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        min_value = inf
        min_value_index = inf
        for j in range(i, len(numbers)):
            if min_value > numbers[j]:
                min_value = numbers[j]
                min_value_index = j

        numbers[min_value_index] = numbers[i]
        numbers[i] = min_value
        input(f"... {numbers=} | {min_value=} | {min_value_index=}")


selection_sort_v1(numbers=[11, 13, 41, 1, 22])
