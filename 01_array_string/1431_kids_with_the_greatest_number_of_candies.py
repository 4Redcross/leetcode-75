# 1431. Kids With the Greatest Number of Candies
# Difficulty: Easy
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        max_candies = []
        for i in candies:
            max_candies.append(i + extraCandies >= highest)

        return max_candies


if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies([2,3,5,1,3], 3))
    # Add your test cases here
