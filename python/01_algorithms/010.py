# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Easy


from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        replace = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[replace] = nums[i]
                replace += 1
        return replace

    def another_sol(self, nums: list[int], val: int) -> int:
        replace = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[replace] = nums[i]
                replace += 1
        return replace


nums = [3, 2, 2, 3]
val = 3
# Output: 2, nums = [2,2,_,_]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


sol = Solution()
print(sol.remove_element(nums, val))

# print(f"{nums=}")
