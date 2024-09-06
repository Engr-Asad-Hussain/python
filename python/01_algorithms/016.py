# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Easy


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        a_len, b_len, carry, total = len(a), len(b), 0, ""
        # range(start, stop, step)
        for i in range(-1, -max(a_len, b_len) - 1, -1):
            try:
                a_val = int(a[i])
            except IndexError:
                a_val = 0

            try:
                b_val = int(b[i])
            except IndexError:
                b_val = 0

            cal = a_val + b_val + carry
            carry = 0
            if cal in (0, 1):
                total = str(cal) + total
            elif cal == 2:
                carry = 1
                total = "0" + total
            elif cal == 3:
                carry = 1
                total = "1" + total

        return str(carry) + total if carry else total

    def another_sol(self, a: str, b: str) -> str:
        s: list[str] = []
        carry: int = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))


a = "11"
b = "1"
# Output: "100"

# a = "1010"
# b = "1011"
# Output: "10101"

# b = "111"
# a = "11"
# Output: "1010"

# b = "0"
# a = "0"
# Output: "0"

print(f"{a=} | {b=}")
sol = Solution()
# print(sol.add_binary(a, b))
print(sol.another_sol(a, b))
