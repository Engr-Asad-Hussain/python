# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Easy


class Solution:
    def is_palindrome(self, x: int) -> bool:
        x_string = str(x)
        y_string = x_string[::-1]
        return x_string == y_string

    def is_palindrome_integer_version(self, x: int) -> bool:
        if x < 0:
            return False

        dividend = x
        tmp = 0
        while dividend:
            quotient, remainder = divmod(dividend, 10)
            tmp = tmp * 10
            tmp = tmp + remainder
            dividend = quotient

        return tmp == x


value = int(input("Please enter a number to be check as Palindrome: "))
sol = Solution()
print(sol.is_palindrome(value))
print(sol.is_palindrome_integer_version(value))
