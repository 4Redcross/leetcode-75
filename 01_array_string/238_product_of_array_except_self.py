# 238. Product of Array Except Self
# Difficulty: Medium
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(n - 2, -1, -1):
            right *= nums[i + 1]
            ans[i] *= right

        return ans


if __name__ == "__main__":
    sol = Solution()
    # Add your test cases here
