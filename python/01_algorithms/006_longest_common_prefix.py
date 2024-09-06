# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Easy


from typing import List


class Solution:
    # Complexity of O(n^2)
    # Problem is, if you check the first letter among all the items in the list
    # Then why to check again the first character on the next iteration?
    def longest_common_prefix(self, string: List[str]) -> str:
        value = string.pop()
        for element in string:
            for i in range(len(value)):
                if value[: i + 1] != element[: i + 1]:
                    value = value[:i]
                    break
        return value

    def another_sol(self, string: List[str]) -> str:
        value = string.pop()
        for i in range(len(value)):
            for word in string:
                if i == len(word) or word[i] != value[i]:
                    return value[:i]
        return value

    # Sort has the time complexity of nlog(n) and for has the time complexity of O(n)
    def another_soll(self, v: List[str]) -> str:
        ans = str()
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


inp = ["fly", "flow", "flight", "flood", "flower", "flowers"]
sol = Solution()
# print(sol.longest_common_prefix(inp))
# print(sol.another_sol(["a", "ab", "abc", "abcd"]))
print(sol.another_soll(inp))
