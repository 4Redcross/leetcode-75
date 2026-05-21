# 334. Increasing Triplet Subsequence
# Difficulty: Medium
# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
            
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([5,4,3,2,1]))
    # Add your test cases here
