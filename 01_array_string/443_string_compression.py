# 443. String Compression
# Difficulty: Medium
# https://leetcode.com/problems/string-compression/

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            
            chars[pos] = char
            pos += 1
            if count > 1:
                count = str(count)
                for ch in count:
                    pos += 1
                    chars[pos] = ch
            i += 1
            
        return pos


if __name__ == "__main__":
    sol = Solution()
    print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    # Add your test cases here
