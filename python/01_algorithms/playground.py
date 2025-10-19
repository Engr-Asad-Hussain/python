from typing import List


def find_indices(nums: List[int], expected_target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the
    two numbers such that they add up to target.

    Reference:
        https://leetcode.com/problems/two-sum/

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    # store all previous values in the dict to match on each iteration
    # also had to store {key, index} so that can be easily fetch index if result found.

    # check on each iteration if value in dict + num == target or counter_part = target - num
    # present in the previous values.

    state = {}
    for index, num in enumerate(nums, start=0):
        counter_part = expected_target - num

        if counter_part in state:
            return [state[counter_part], index]
        else:
            state[num] = index


# result = find_indices(nums=[2, 7, 11, 15], expected_target=17)
# print(f"{result=}")


def is_palindrome_number_v1(x: int) -> bool:
    """
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Reference:
        https://leetcode.com/problems/palindrome-number/description/

    Example:
        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.

    Constraints:
        Could you solve it without converting the integer to a string?
    """
    x_string = str(x)
    return x_string == x_string[::-1]


# result = is_palindrome_number_v1(x=121)
# print(f"{result=}")


def is_palindrome_number_v2(x: int) -> bool:
    """
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Reference:
        https://leetcode.com/problems/palindrome-number/description/

    Example:
        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.

    Constraints:
        Could you solve it without converting the integer to a string?
    """
    if x < 0:
        return False
    divisor = 10
    dividend = x
    # detail description on divisor, dividend, remainder, and
    # quotient https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/jayshree-dividend-divisor-quotient-remainder-formula-01-1622711306.png
    reverse_x = 0
    while dividend:
        quotient, remainder = divmod(dividend, divisor)
        reverse_x = reverse_x * 10 + remainder
        dividend = quotient

    return reverse_x == x


# result = is_palindrome_number_v2(x=-121)
# print(f"{result=}")


def roman_to_integer(roman_string: str):
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two ones added together.
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
    which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

    Example 1:
        Input: s = "III"
        Output: 3
        Explanation: III = 3.

    Example 2:
        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.

    Example 3:
        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Reference:
        https://leetcode.com/problems/roman-to-integer/description/
    """
    total = 0
    previous_character = ""
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for character in roman_string:
        total = total + roman_map[character]

        if previous_character + character in ("IV", "IX"):
            total = total - 2

        elif previous_character + character in ("XL", "XC"):
            total = total - 20

        elif previous_character + character in ("CD", "CM"):
            total = total - 200

        # update the previous character state
        previous_character = character

    return total


# result = roman_to_integer(roman_string="III")  # 3
# result = roman_to_integer(roman_string="IV") # 4
# result = roman_to_integer(roman_string="XXIV")  # 24
# result = roman_to_integer(roman_string="IX")  # 9
# result = roman_to_integer(roman_string="LXX")  # 70
# result = roman_to_integer(roman_string="XL")  # 40
# result = roman_to_integer(roman_string="LVIII")  # 58
# result = roman_to_integer(roman_string="MCMXCIV")  # 1994
# print(f"{result=}")


def longest_common_prefix_v1(items: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"

    Reference:
        https://leetcode.com/problems/longest-common-prefix/
    """
    common = items[-1]
    for i in range(len(items) - 1):
        for j in range(len(common)):
            if common[: j + 1] != items[i][: j + 1]:
                common = common[:j]
                break
    return common


# result = longest_common_prefix_v1(items=["aaa", "aa", "aaa"])  # aa
# result = longest_common_prefix_v1(items=["flight", "flow", "flower"])  # fl
# result = longest_common_prefix_v1(items=["dog", "racecar", "car"])  # ""
# result = longest_common_prefix_v1(items=["ab", "abc"])  # "ab"
# print(f"{result=}")


def longest_common_prefix_v2(items: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"

    Reference:
        https://leetcode.com/problems/longest-common-prefix/
    """
    # if we can sort the items list
    # then we only have to compare the characters of first index and last index items

    # sort the items; .sort() returns None because it modifies original List
    items.sort()
    first_item = items[0]
    last_item = items[-1]
    first_item_len = len(first_item)
    last_item_len = len(last_item)
    ans = str()
    for i in range(min(first_item_len, last_item_len)):
        if first_item[i] != last_item[i]:
            return ans
        ans = ans + first_item[i]
    return ans


# result = longest_common_prefix_v2(items=["flight", "flow", "flower"])  # fl
# result = longest_common_prefix_v2(
#     items=["flo", "flower", "flew", "foot", "flight"]
# )  # "f"
# print(f"{result=}")


def valid_parentheses_v1(string: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.

    Example 1:
        Input: s = "()"
        Output: true

    Example 2:
        Input: s = "()[]{}"
        Output: true

    Example 3:
        Input: s = "(]"
        Output: false

    Reference:
        https://leetcode.com/problems/valid-parentheses/
    """
    stack: List[str] = []
    for s in string:
        if s in "({[":
            stack.append(s)

        else:
            if stack == []:
                return False

            if s == ")" and stack[-1] != "(":
                return False

            elif s == "}" and stack[-1] != "{":
                return False

            elif s == "]" and stack[-1] != "[":
                return False

            else:
                stack.pop()

    return True if stack == [] else False


# result = valid_parentheses_v1(string=r"()")  # True
# result = valid_parentheses_v1(string=r"()[]{}")  # True
# result = valid_parentheses_v1(string=r"(]")  # False
# result = valid_parentheses_v1(string=r"((")  # False
# result = valid_parentheses_v1(string=r"(){}}{")  # False
# result = valid_parentheses_v1(string=r"([)]")  # False
# print(f"{result=}")


def valid_parentheses_v2(string: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.

    Example 1:
        Input: s = "()"
        Output: true

    Example 2:
        Input: s = "()[]{}"
        Output: true

    Example 3:
        Input: s = "(]"
        Output: false


    Reference:
        https://leetcode.com/problems/valid-parentheses/
    """
    stack: List[str] = []
    for s in string:
        if s in "({[":
            stack.append(s)

        else:
            if (
                not stack
                or (s == ")" and stack[-1] != "(")
                or (s == "}" and stack[-1] != "{")
                or (s == "]" and stack[-1] != "[")
            ):
                return False
            else:
                stack.pop()

    return True if stack == [] else False


# result = valid_parentheses_v2(string=r"()")  # True
# result = valid_parentheses_v2(string=r"()[]{}")  # True
# result = valid_parentheses_v2(string=r"(]")  # False
# result = valid_parentheses_v2(string=r"((")  # False
# result = valid_parentheses_v2(string=r"(){}}{")  # False
# result = valid_parentheses_v2(string=r"([)]")  # False
# print(f"{result=}")


def remove_duplicates_from_sorted_array_v1(nums: List[int]) -> List[int]:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates
    in-place such that each unique element appears only once. The relative order of the
    elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need
    to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements
    in the order they were present in nums initially. The remaining elements of nums are not
    important as well as the size of nums.
    Return k.

    Custom Judge:
        The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        If all assertions pass, then your solution will be accepted.

    Example 1:
        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two elements of nums
        being 1 and 2 respectively. It does not matter what you leave beyond the returned
        k (hence they are underscores).

    Example 2:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of
        nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond
        the returned k (hence they are underscores).
    """
    # loop through the nums
    # check if the num is present in expected nums
    # if not present append in expected nums
    # if present?
    # at this point expected nums must only contains unique num with unequal length compared to nums

    counter = 0
    # range definition: range(start=0, stop, step)
    for i in range(0, len(nums)):
        if nums[i] == "_":
            break

        counter += 1
        j = i + 1
        while True:
            try:
                assert nums[j] != "_"
                assert nums[i] == nums[j]
            except (AssertionError, IndexError):
                break

            if nums[j] in nums[i + 1 :]:
                nums.pop(j)
                nums.append("_")
            else:
                j += 1
    # print(f"{nums=}")
    return counter


# result = remove_duplicates_from_sorted_array_v1(nums=[])
# result = remove_duplicates_from_sorted_array_v1(nums=[1])
# result = remove_duplicates_from_sorted_array_v1(nums=[1, 1])
# result = remove_duplicates_from_sorted_array_v1(nums=[1, 2])
# result = remove_duplicates_from_sorted_array_v1(nums=[1, 1, 2])
# result = remove_duplicates_from_sorted_array_v1(nums=[1, 1, 2, 2, 2, 3, 3])
# result = remove_duplicates_from_sorted_array_v1(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# result = remove_duplicates_from_sorted_array_v1(nums=[0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# print(f"{result=}")


def remove_duplicates_from_sorted_array_v2(nums: List[int]) -> List[int]:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates
    in-place such that each unique element appears only once. The relative order of the
    elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need
    to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements
    in the order they were present in nums initially. The remaining elements of nums are not
    important as well as the size of nums.
    Return k.

    Custom Judge:
        The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        If all assertions pass, then your solution will be accepted.

    Example 1:
        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two elements of nums
        being 1 and 2 respectively. It does not matter what you leave beyond the returned
        k (hence they are underscores).

    Example 2:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of
        nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond
        the returned k (hence they are underscores).
    """
    # loop through the nums
    # check if the num is present in expected nums
    # if not present append in expected nums
    # if present?
    # at this point expected nums must only contains unique num with unequal length compared to nums

    replace = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[replace] = nums[i]
            replace += 1
    return replace


# result = remove_duplicates_from_sorted_array_v2(nums=[])
# result = remove_duplicates_from_sorted_array_v2(nums=[1])
# result = remove_duplicates_from_sorted_array_v2(nums=[1, 1])
# result = remove_duplicates_from_sorted_array_v2(nums=[1, 2])
# result = remove_duplicates_from_sorted_array_v2(nums=[1, 1, 2])
# result = remove_duplicates_from_sorted_array_v2(nums=[1, 1, 2, 2, 2, 3, 3])
# result = remove_duplicates_from_sorted_array_v2(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# result = remove_duplicates_from_sorted_array_v2(nums=[0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# print(f"{result=}")


def remove_elements(nums: List[int], val: int) -> int:
    replace = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            for j in range(i + 1, len(nums)):
                if nums[j] != val:
                    break
            nums[i] = nums[j]
            replace += 1
    # print(f"{nums=}")
    return replace


# result = remove_elements(nums=[3, 2, 2, 3], val=3)
# result = remove_elements(nums=[3, 3, 2, 2], val=3)
result = remove_elements(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
# print(f"{result=}")


def remove_duplicates_from_list(nums: List[int]) -> List[int]:
    i = 0
    while True:
        try:
            if nums[i] in nums[i + 1 :]:
                nums.pop(i)
            else:
                i += 1
        except IndexError:
            break
    return nums


# result = remove_duplicates_from_list(nums=[2, 3, 2, 5, 6, 8, 3, 3, 3])
# print(f"{result=}")


def bubble_sort_algorithm_v1(numbers: List[int]) -> List[int]:
    """
    Used bubble sort algorithm to sort the numbers in a list
    using comparison operator. Each pair of elements is compared
    and swapped if they are not in order.
    array:   14 33 27 35 10
    index:   0  1  2  3  4
    pointer: ↑  ↑ (14 > 35 if True swap)
    """
    for i in range(len(numbers)):
        # i=0=14 [14, 33, 27, 35, 10]
        # i=1=14 [35, 14, 27, 33, 10]
        # i=2=27 [14, 35, 27, 33, 10]
        # i=3=33 [14, 27, 35, 33, 10]
        # i=4=10 [14, 27, 33, 35, 10]
        for j in range(len(numbers)):
            # i=0=14 < j=0=14
            # i=0=14 < j=1=33 [33, 14, 27, 35, 10]
            # i=0=33 < j=2=27
            # i=0=33 < j=3=35 [35, 14, 27, 33, 10]
            # i=0=35 < j=4=10
            # ---
            # i=1=14 < j=0=35 [14, 35, 27, 33, 10]
            # i=1=35 < j=1=35
            # i=1=35 < j=2=27
            # i=1=35 < j=3=33
            # i=1=35 < j=4=10
            # ---
            # i=2=27 < j=0=14
            # i=2=27 < j=1=35 [14, 27, 35, 33, 10]
            # i=2=35 < j=2=35
            # i=2=35 < j=3=33
            # i=2=35 < j=4=10
            # ---
            # i=3=33 < j=0=14
            # i=3=33 < j=1=27
            # i=3=33 < j=2=35 [14, 27, 33, 35, 10]
            # i=3=35 < j=3=35
            # i=3=35 < j=4=10
            # ---
            # i=4=10 < j=0=14 [10, 27, 33, 35, 14]
            # i=4=14 < j=1=27 [10, 14, 33, 35, 27]
            # i=4=27 < j=2=33 [10, 14, 27, 35, 33]
            # i=4=33 < j=3=35 [10, 14, 27, 33, 35]
            # i=4=35 < j=4=35
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

        # [35, 14, 27, 33, 10]
        # [14, 35, 27, 33, 10]
        # [14, 27, 35, 33, 10]
        # [14, 27, 33, 35, 10]
        # [10, 14, 27, 33, 35]
        input(f"Please enter to continue: {numbers} ...")


def bubble_sort_algorithm_v2(numbers: List[int]) -> List[int]:
    """
    [5, 3, 8, 4, 2]

    First pass:
    *   Compare 5 & 3 → swap → [3, 5, 8, 4, 2]
    *   Compare 5 & 8 → OK
    *   Compare 8 & 4 → swap → [3, 5, 4, 8, 2]
    *   Compare 8 & 2 → swap → [3, 5, 4, 2, 8] ✅ largest is at the end

    Second pass:
    *   Compare 3 & 5 → OK
    *   Compare 5 & 4 → swap → [3, 4, 5, 2, 8]
    *   Compare 5 & 2 → swap → [3, 4, 2, 5, 8]

    Third pass:
    *   Compare 3 & 4 → OK
    *   Compare 4 & 2 → swap → [3, 2, 4, 5, 8]

    Fourth pass:
    *   Compare 3 & 2 → swap → [2, 3, 4, 5, 8] ✅ now sorted
    """
    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Swap
                swapped = True
        if swapped is False:
            break  # When the elements are already in sorted position


# bubble_sort_algorithm_v1(numbers=[14, 33, 27, 35, 10])
bubble_sort_algorithm_v2(numbers=[14, 33, 27, 35, 10])
# bubble_sort_algorithm_v2(numbers=[10, 14, 27, 33, 35])
