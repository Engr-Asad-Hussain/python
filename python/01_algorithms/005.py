# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Easy

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# IV            4
# IX            9
# XL            40
# XC            90
# CD            400
# CM            900


class Solution:
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def roman_to_int(self, s: str) -> int:
        sum = 0
        previous_value = ""
        for value in s:
            if previous_value:
                if value in ("V", "X") and previous_value == "I":
                    sum += self.mapping[value] - self.mapping[previous_value]
                    previous_value = ""
                    continue

                if value in ("L", "C") and previous_value == "X":
                    sum += self.mapping[value] - self.mapping[previous_value]
                    previous_value = ""
                    continue

                if value in ("D", "M") and previous_value == "C":
                    sum += self.mapping[value] - self.mapping[previous_value]
                    previous_value = ""
                    continue

                sum += self.mapping[previous_value]
                previous_value = value

            elif value in ("I", "X", "C"):
                previous_value = value
                continue

            else:
                sum += self.mapping[value]

        if previous_value:
            sum += self.mapping[previous_value]

        return sum

    def roman_to_int_improve(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            current_value = self.mapping[s[i]]
            try:
                next_value = self.mapping[s[i + 1]]
            except IndexError:
                next_value = current_value

            if current_value < next_value:
                ans -= current_value
            else:
                ans += current_value

        return ans

    def another_sol(self, s: str) -> int:
        string = (
            s.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )

        ans = 0
        for value in string:
            ans += self.mapping[value]

        return ans


sol = Solution()
# sol.roman_to_int_improve("XX")
# sol.roman_to_int_improve("V")
# sol.roman_to_int_improve("LVIII")
# sol.roman_to_int_improve("MCMXCIV")
# print(sol.roman_to_int_improve("IX"))
# print(sol.another_sol("IX"))
# print(sol.another_sol("V"))
# print(sol.another_sol("LVIII"))
# sol.another_sol("MCMXCIV")
sol.another_sol("VIII")
