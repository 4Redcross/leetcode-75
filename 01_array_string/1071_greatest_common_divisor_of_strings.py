# 1071. Greatest Common Divisor of Strings
# Difficulty: Easy
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    """ Initial Approach
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a, b = len(str1), len(str2)
        largest = ""
        short = min(a, b)
        for i in range(1, short + 1):
            xa = a / i
            xb = b / i
            if xa.is_integer and xb.is_integer:
                if str1[:i] * int(xa) == str1 and str2[:i] * int(xb) == str2:
                    largest = str1[:i]

        return largest
    """
    # The initial approach made was running at O(n^2) as we iterated from 1 to short
    # and for each iteration we multiplied the string and compared after
    # Better approach involves checking for equality between strings
    # usng converse additions
    # Then using the [Euclidean algorithm](https://math.stackexchange.com/a/3379763) to find GCD between lengths of string!

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b

        return str1[:a]


if __name__ == "__main__":
    sol = Solution()
    print("ANS: " + sol.gcdOfStrings("ABCABC", "ABC"))
    # Add your test cases here
