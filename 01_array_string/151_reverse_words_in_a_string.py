# 151. Reverse Words in a String
# Difficulty: Medium
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words.reverse()
        return " ".join(filter(("").__ne__, words))

        # Or just use return " ".join(s.split()[::-1])
        # split automatically ignores all whitespaces, [::-1] reverses the list



if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("a good   example"))
    # Add your test cases here
