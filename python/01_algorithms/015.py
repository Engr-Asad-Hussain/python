# 66. Plus One
# https://leetcode.com/problems/plus-one/
# Easy


from typing import List


class Solution:
    # Beat 89.2%
    def plus_one(self, digits: List[int]) -> List[int]:
        answer = 0
        for digit in digits:
            answer = answer * 10
            answer += digit
        answer = answer + 1
        from collections import deque

        output: deque[int] = deque()
        divident = answer
        while divident:
            quotient, remainder = divmod(divident, 10)
            output.appendleft(remainder)
            divident = quotient
        return list(output)

    # Beat 62.8%
    def another_sol(self, digits: List[int]) -> List[int]:
        from collections import deque

        answer: deque[int] = deque()
        last = digits[-1] + 1
        carry = 0
        if last > 9:
            carry = 1
            last = 0
        answer.appendleft(last)
        for i in range(len(digits) - 2, -1, -1):
            last = digits[i] + carry
            if last > 9:
                carry = 1
                answer.appendleft(0)
            else:
                carry = 0
                answer.appendleft(last)

        if carry == 1:
            answer.appendleft(1)
        return list(answer)


digits = [1, 2, 3]
# Output: [1,2,4]

# digits = [4, 3, 2, 1]
# Output: [4,3,2,2]

# digits = [9]
# Output: [1,0]

print(f"{digits=}")
sol = Solution()
# print(sol.plus_one(digits))
print(sol.another_sol(digits))
