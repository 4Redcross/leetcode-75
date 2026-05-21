# 605. Can Place Flowers
# Difficulty: Easy
# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        
        return n <= 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers([1,0,0,0,1,0,0], 2))
