# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Easy


class Solution:
    def length_of_last_word(self, s: str) -> int:
        index = -1
        length = 0
        while True:
            try:
                value = s[index]
            except IndexError:
                return length

            if value != " ":
                length += 1
            else:
                if length > 0:
                    return length
            index = index - 1


s = "Hello World"
# Output: 5

s = "   fly me   to   the moon  "
# Output: 4

s = "luffy is still joyboy"
# Output: 6

s = "a"
# Output: 6

sol = Solution()
print(sol.length_of_last_word(s))
