# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Easy


from typing import List


class Solution:
    # O(n) time complexity because iterate over the end in the worst-case
    def search_insert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1

    # log(n) time complexity because binary search
    def another_sol(self, nums: List[int], target: int) -> int:
        # Starting Pointer
        sp = 0

        # Ending Pointer
        ep = len(nums) - 1
        while sp <= ep:
            mid = (sp + ep) // 2
            print(
                f"{sp=} | {ep=} | (sp + ep) / 2 => ({sp} + {ep}) / 2 => {mid=} | {nums[mid]=} | {target=}"
            )
            input()

            if nums[mid] < target:
                sp = mid + 1
                print(
                    f"... {mid=} | nums[mid] < target => {nums[mid]} < {target} => sp = mid + 1 = {sp} | Target is greater than current value i.e., increase the sp."
                )
            elif nums[mid] > target:
                ep = mid - 1
                print(
                    f"... {mid=} | nums[mid] > target => {nums[mid]} > {target} => ep = mid - 1 = {ep} | Target is less than current value i.e., reduce the ep."
                )
            else:
                return mid
        return sp


nums = [1, 3, 5, 6]
target = 5
# Output = 2

nums = [1, 3, 5, 6]
target = 2
# Output = 1

# nums = [1, 3, 5, 6]
# target = 7
# # Output = 4

# nums = [1, 3, 5, 6]
# target = 0
# # Output = 0

# nums = [1, 3, 5, 6, 8, 10, 12]
# target = 8

sol = Solution()
print(f"{nums=} | {target=}")
# print(sol.search_insert(nums, target))
print(sol.another_sol(nums, target))
