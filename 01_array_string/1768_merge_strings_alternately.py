# 1768. Merge Strings Alternately
# Difficulty: Easy
# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    """ Initial Approach
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short = min(len(word1), len(word2))
        ans = ""
        for i in range(0, short):
            ans += word1[i] + word2[i]
        
        if(len(word1) > len(word2)):
            ans += word1[short:]
        else:
            ans += word2[short:]
        
        return ans
    """
    # The better approach is to make use of a list and .append()
    # In python, strings are immutable so for our previous solution every time that we did
    # `ans += ...`` we were objectively creating a brand new string in memory 
    # and copying characters from ans into it and then appending new characters
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short = min(len(word1), len(word2))
        ans = []
        for i in range(0, short):
            ans.append(word1[i])
            ans.append(word2[i])
        
        if(len(word1) > len(word2)):
            ans.append(word1[short:])
        else:
            ans.append(word2[short:])
        
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternately("abcd", "pq"))
