from typing import List


def bubble_sort_algorithm_v1(numbers: List[int]) -> List[int]:
    """
    Used bubble sort algorithm to sort the numbers in a list
    using comparison operator. Each pair of elements is compared
    and swapped if they are not in order.
    array:   14 33 27 35 10
    index:   0  1  2  3  4
    pointer: ↑  ↑ (14 > 35 if True swap)
    """
    for i in range(len(numbers)):
        # i=0=14 [14, 33, 27, 35, 10]
        # i=1=14 [35, 14, 27, 33, 10]
        # i=2=27 [14, 35, 27, 33, 10]
        # i=3=33 [14, 27, 35, 33, 10]
        # i=4=10 [14, 27, 33, 35, 10]
        for j in range(len(numbers)):
            # i=0=14 < j=0=14
            # i=0=14 < j=1=33 [33, 14, 27, 35, 10]
            # i=0=33 < j=2=27
            # i=0=33 < j=3=35 [35, 14, 27, 33, 10]
            # i=0=35 < j=4=10
            # ---
            # i=1=14 < j=0=35 [14, 35, 27, 33, 10]
            # i=1=35 < j=1=35
            # i=1=35 < j=2=27
            # i=1=35 < j=3=33
            # i=1=35 < j=4=10
            # ---
            # i=2=27 < j=0=14
            # i=2=27 < j=1=35 [14, 27, 35, 33, 10]
            # i=2=35 < j=2=35
            # i=2=35 < j=3=33
            # i=2=35 < j=4=10
            # ---
            # i=3=33 < j=0=14
            # i=3=33 < j=1=27
            # i=3=33 < j=2=35 [14, 27, 33, 35, 10]
            # i=3=35 < j=3=35
            # i=3=35 < j=4=10
            # ---
            # i=4=10 < j=0=14 [10, 27, 33, 35, 14]
            # i=4=14 < j=1=27 [10, 14, 33, 35, 27]
            # i=4=27 < j=2=33 [10, 14, 27, 35, 33]
            # i=4=33 < j=3=35 [10, 14, 27, 33, 35]
            # i=4=35 < j=4=35
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

        # [35, 14, 27, 33, 10]
        # [14, 35, 27, 33, 10]
        # [14, 27, 35, 33, 10]
        # [14, 27, 33, 35, 10]
        # [10, 14, 27, 33, 35]
        input(f"Please enter to continue: {numbers} ...")


def bubble_sort_algorithm_v2(numbers: List[int]) -> List[int]:
    """
    [5, 3, 8, 4, 2]

    First pass:
    *   Compare 5 & 3 → swap → [3, 5, 8, 4, 2]
    *   Compare 5 & 8 → OK
    *   Compare 8 & 4 → swap → [3, 5, 4, 8, 2]
    *   Compare 8 & 2 → swap → [3, 5, 4, 2, 8] ✅ largest is at the end

    Second pass:
    *   Compare 3 & 5 → OK
    *   Compare 5 & 4 → swap → [3, 4, 5, 2, 8]
    *   Compare 5 & 2 → swap → [3, 4, 2, 5, 8]

    Third pass:
    *   Compare 3 & 4 → OK
    *   Compare 4 & 2 → swap → [3, 2, 4, 5, 8]

    Fourth pass:
    *   Compare 3 & 2 → swap → [2, 3, 4, 5, 8] ✅ now sorted
    """
    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Swap
                swapped = True
        if swapped is False:
            break  # When the elements are already in sorted position

    input(f"Please enter to continue: {numbers} ...")


# bubble_sort_algorithm_v1(numbers=[14, 33, 27, 35, 10])
bubble_sort_algorithm_v2(numbers=[14, 33, 27, 35, 10])
# bubble_sort_algorithm_v2(numbers=[10, 14, 27, 33, 35])
