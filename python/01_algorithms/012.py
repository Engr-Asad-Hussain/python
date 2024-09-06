# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Easy


from operator import ne


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        # calculate length of needle
        # iterate over haystack
        # match offset of haystack with needle
        nl = len(needle)
        for i in range(len(haystack)):
            if haystack[i : i + nl] == needle:
                return i
        return -1

    def another_sol(self, haystack: str, needle: str) -> int:
        # needle = "issip"
        # needle = "01234"
        lps = [0] * len(needle)  # [0, 0, 0, 0, 0]
        pre = 0
        for i in range(1, len(needle)):
            # iteration=1 | i=1 | pre=0 | needle[i]=s | needle[pre]=i
            # iteration=2 | i=2 | pre=0 | needle[i]=s | needle[pre]=i
            # iteration=3 | i=3 | pre=0 | needle[i]=i | needle[pre]=i
            # iteration=4 | i=4 | pre=1 | needle[i]=p | needle[pre]=s

            # iteration=1 | False (0>0)
            # iteration=2 | False (0>0)
            # iteration=3 | False (0>0)
            # iteration=4 | False (1>0 and p!=s)
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre - 1]
                # pre=lps[1-1]=lps[0] = 0

            # iteration=1 | False (i==s)
            # iteration=2 | False (i==s)
            # iteration=3 | True  (i==i)
            # iteration=4 | False (i==p) (pre modified)
            if needle[pre] == needle[i]:
                pre += 1
                # pre=1

                lps[i] = pre
                # lps=[0, 0, 0, 1, 0]

        print(lps)
        # final=lps=[0, 0, 0, 1, 0]
        n = 0
        # haystack = "mississippi"
        # haystack = "0123456789(10)"
        # needle = "issip"
        # needle = "01234"
        for h in range(len(haystack)):
            # iteration=1 | h=0 | n=0 | needle[n]=i | haystack[h]=m | len(needle)=5
            # iteration=2 | h=1 | n=1 | needle[n]=s | haystack[h]=i | len(needle)=5
            # iteration=3 | h=2 | n=1 | needle[n]=s | haystack[h]=s | len(needle)=5
            # iteration=4 | h=3 | n=2 | needle[n]=s | haystack[h]=s | len(needle)=5
            # iteration=5 | h=4 | n=3 | needle[n]=i | haystack[h]=i | len(needle)=5
            # iteration=6 | h=5 | n=4 | needle[n]=p | haystack[h]=s | len(needle)=5
            # iteration=7 | h=6 | n=0 | needle[n]=i | haystack[h]=s | len(needle)=5
            # iteration=8 | h=7 | n=0 | needle[n]=i | haystack[h]=i | len(needle)=5
            # iteration=9 | h=8 | n=1 | needle[n]=s | haystack[h]=i | len(needle)=5

            # iteration=1 | False (0>0)
            # iteration=2 | True  (1>0 and s!=i)
            # iteration=3 | False (1>0 and s!=s)
            # iteration=4 | False (2>0 and s!=s)
            # iteration=5 | False (3>0 and i!=i)
            # iteration=6 | False (4>0 and p!=s)
            # iteration=7 | False (0>0)
            # iteration=8 | False (0>0)
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n - 1]
                # n = lps[1 - 1] = lps[0] = 0
                # n = lps[4 - 1] = lps[3] = 0

            # iteration=1 | False (i==m)
            # iteration=2 | True  (i==i)
            # iteration=3 | True  (s==s)
            # iteration=4 | True  (s==s)
            # iteration=5 | True  (i==i)
            # iteration=6 | False (i==s)
            # iteration=7 | False (i==s)
            # iteration=8 | True  (i==i)
            if needle[n] == haystack[h]:
                n += 1
                # n=1
                # n=2
                # n=3
                # n=4
                # n=1

            # iteration=1 | False (0==5)
            # iteration=2 | False (1==5)
            # iteration=3 | False (2==5)
            # iteration=4 | False (3==5)
            # iteration=5 | False (4==5)
            # iteration=6 | False (0==5)
            # iteration=7 | False (0==5)
            # iteration=8 | False (1==5)
            if n == len(needle):
                return h - n + 1
        return -1


haystack = "sadbutsad"
needle = "sad"
# Output: 0

haystack = "leetcode"
needle = "leeto"
# # Output: -1

haystack = "mississippi"
needle = "issip"

haystack = "abcabababc"
needle = "babc"


sol = Solution()
# print(sol.str_str(haystack, needle))
# print(sol.another_sol(haystack, needle))
