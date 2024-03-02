# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Easy


class Solution:
    def floor_sqrt(self, x: int) -> int:
        if x in (0, 1):
            return x

        i = 1
        result = 1
        while result <= x:
            i += 1
            result = i * i

        return i - 1

    def binary_search(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square < x:
                left = mid + 1
            else:
                return mid
        return right


x = 4
# Output = 2

x = 8
# Output = 2 (2.82; round it down to nearest integer)

sol = Solution()
# print(sol.floor_sqrt(x))
print(sol.binary_search(x))


# You can always run a sequential search—scanning the array from the beginning to the end—on
# the array. But if the array is sorted, running the binary search algorithm is
# much more efficient.


def linear_search(nums: list[int], target: int) -> bool:
    """
    Performs on unsorted iteratables.\n
    Args:
        - `nums` (list[int]): The list of integers.
        - `target` int: the target value to be search.
    """

    for val in nums:
        if val == target:
            return True
    return False


def binary_search(nums: list[int], target: int) -> tuple[int, int] | bool:
    """
    Performs on sorted iteratables.\n
    Args:
        - `nums` (list[int]): The list of integers.
        - `target` int: the target value to be search.
    """

    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        mid = nums[mid_pointer]
        if mid > target:
            right_pointer = mid_pointer - 1
        elif mid < target:
            left_pointer = mid_pointer + 1
        else:
            return mid_pointer, mid

    return False


# nums = [1, 20, 89, 42, 29, 11, 5]
# print(linear_search(nums, 421))

# nums = [2, 5, 7, 11, 14, 21, 27, 30, 36]
# print(binary_search(nums, -271))
