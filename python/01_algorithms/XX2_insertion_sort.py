from typing import List


def insertion_sort_v1(numbers: List[int]) -> List[int]:
    """
    Suppose we have this array:
    [5, 3, 4, 1, 2]

    Start with index 1 (element 3)
    *   Compare with 5, shift 5 → Insert 3 before it
    *   → [3, 5, 4, 1, 2]

    Next element 4
    *    Compare with 5 (shift), then compare with 3 → insert after 3
    *   → [3, 4, 5, 1, 2]

    Next 1
    *   Shift 5, 4, 3 → insert at beginning
    *   → [1, 3, 4, 5, 2]

    Next 2
    *   Compare and shift → insert after 1
    *   → [1, 2, 3, 4, 5]
    """
    # numbers=[5, 3, 4, 1, 2]

    for i in range(1, len(numbers)):  # Assume index 0 (element 5) is already sorted!
        # i=1=3 [5, 3, 4, 1, 2]
        # i=2=4 [3, 5, 4, 1, 2]
        # i=3=1 [3, 4, 5, 1, 2]
        # i=4=2 [1, 3, 4, 5, 2]

        # range signature is start, end, step (i, 1) → end index is exclusive
        for j in range(i, 0, -1):
            # j=0=5 > j=1=3 [3, 5, 4, 1, 2]
            # j=1=5 > j=2=4 [3, 4, 5, 1, 2]
            # j=0=3 > j=1=4
            # j=2=5 > j=3=1 [3, 4, 1, 5, 2]
            # j=1=4 > j=2=1 [3, 1, 4, 5, 2]
            # j=0=3 > j=1=1 [1, 3, 4, 5, 2]
            # j=3=5 > j=4=2 [1, 3, 4, 2, 5]
            # j=2=4 > j=3=2 [1, 3, 2, 4, 5]
            # j=1=3 > j=2=2 [1, 2, 3, 4, 5]
            # j=0=1 > j=1=2
            if numbers[j - 1] > numbers[j]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]

        # [3, 5, 4, 1, 2]
        # [3, 4, 5, 1, 2]
        # [1, 3, 4, 5, 2]
        # [1, 2, 3, 4, 5]
        input(f"... {numbers=}")


insertion_sort_v1(numbers=[5, 3, 4, 1, 2])
