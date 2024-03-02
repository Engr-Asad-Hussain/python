# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Easy


class Solution:
    def remove_duplicates(self, nums: list[int | str]) -> int:
        map = {}
        i = 0
        counter = 0
        while i < len(nums):
            item = nums[i]
            if item in map:
                nums.pop(i)
                nums.append("_")
            else:
                if item != "_":
                    map[item] = item
                    counter += 1
                i += 1
        return counter

    def another_sol(self, nums: list[int]) -> int:
        replace = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace


# nums = [1, 1, 2]
# output = [1, 2, _]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# output = [0, 1, 2, 3, 4, _, _, _, _, _]

sol = Solution()
# print(sol.remove_duplicates(nums))
print(sol.another_sol(nums))

# print(f"{nums=}")
