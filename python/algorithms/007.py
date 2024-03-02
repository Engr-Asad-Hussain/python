# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Easy


from typing import Any


class Solution:
    def is_valid(self, string: str) -> bool:
        str_len = len(string)
        if str_len == 0:
            return False

        temp: list[str] = []
        for s in string:
            if s in ("(", "{", "["):
                temp.append(s)
                continue

            try:
                last_item = temp.pop()
            except IndexError:
                return False

            if last_item == "[" and s == "]":
                continue
            if last_item == "{" and s == "}":
                continue
            if last_item == "(" and s == ")":
                continue

            return False
        return True if len(temp) == 0 else False

    def another_version(self, string: str):
        stack: list[str] = []
        for c in string:
            if c in "({[":
                stack.append(c)
            else:
                if (
                    not stack
                    or (c == ")" and stack[-1] != "(")
                    or (c == "}" and stack[-1] != "{")
                    or (c == "]" and stack[-1] != "[")
                ):
                    return False
                stack.pop()
        return not stack


# string = ""
string = "}"
# string = "["
# string = "(("
# string = "()"
# string = "{}"
# string = "{}[]"
# string = "{}[]()"
# string = "{}[](]"
# string = "{}[}(]"
string = "{[]}"
sol = Solution()
print(sol.is_valid(string))
print(sol.another_version(string))
