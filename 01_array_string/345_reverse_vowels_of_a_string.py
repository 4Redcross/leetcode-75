# 345. Reverse Vowels of a String
# Difficulty: Easy
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    """ Initial Approach
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        present = []
        for c in s:
            if c in vowels:
                present.append(c)
        
        ans = []
        for c in s:
            if c in vowels:
                ans.append(present.pop())
            else:
                ans.append(c)
        return "".join(ans)
    """
    # We can improve our approach by making `vowels` a set
    # And using Two pointer approach instead of iterating through s twice

    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
                
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("leetcode"))
    # Add your test cases here
