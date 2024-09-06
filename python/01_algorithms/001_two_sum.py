from timeit import default_timer
from typing import Any

nums: list[int] = [4, 4, 4, 5, 5, 9, 7]
target: int = 10


def index_filter(nums: list[int], target: int) -> tuple[int, int] | None:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            # print(f"{i=}, {nums[i]=}, {j=}, {nums[j]=}")
            if nums[i] + nums[j] == target:
                return i, j


# https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented/44509302#44509302
def index_filter_optimized(nums: list[int], target: int) -> Any:
    hash_table = {}
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return hash_table[complement], i
        hash_table[nums[i]] = i


def main():
    start_timer = default_timer()
    indexes = index_filter(nums, target)
    end_timer = default_timer()
    print("Numbers are %s " % nums)
    print("Target is %s " % target)
    print(indexes)
    print("Total complexity is O(n^2)")
    print("Runtime is %s " % (end_timer - start_timer))
    print()

    start_timer = default_timer()
    indexes = index_filter_optimized(nums, target)
    end_timer = default_timer()
    print("Numbers are %s " % nums)
    print("Target is %s " % target)
    print(indexes)
    print("Total complexity is O(n)")
    print("Runtime is %s " % (end_timer - start_timer))


if __name__ == "__main__":
    main()
