# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Easy

from typing import List


class Solution:
    # Hash Set Approach
    # The time complexity of this approach is O(n), where n is the length of the array.
    def contains_duplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Hash Map Approach
    # The time complexity of this approach is O(n), where n is the length of the array.
    def contains_duplicate_map(self, nums: List[int]) -> bool | None:
        temp = {}
        for num in nums:
            try:
                temp[num]
                return True
            except KeyError:
                temp[num] = 1


nums = [1, 2, 3, 4, 5]
sol = Solution()
print(sol.contains_duplicate(nums))
print(sol.contains_duplicate_map(nums))
