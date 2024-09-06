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
        # replace = 1: This variable keeps track of the index where
        # non-duplicate elements should be placed in the modified array.
        # We start from index 1 because the element at index 0 is always
        # unique (since it's the first element).
        replace = 1

        # for i in range(1, len(nums)):: This loop iterates over the array
        # starting from the second element (index 1) to the end of the array.
        for i in range(1, len(nums)):

            # if nums[i] != nums[i - 1]:: This condition checks if the current
            # element (nums[i]) is different from the previous element (nums[i - 1]).
            # If they are not equal, it means the current element is not a
            # duplicate.
            if nums[i] != nums[i - 1]:

                # nums[replace] = nums[i]: If the current element is not a
                # duplicate, it's copied to the replace index in the array.
                # Since replace initially starts at 1, this effectively moves
                # non-duplicate elements to the beginning of the array.
                nums[replace] = nums[i]

                # replace += 1: After copying the non-duplicate element, we increment
                # replace so that the next non-duplicate element will be placed at the
                # next available position in the modified array.
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
