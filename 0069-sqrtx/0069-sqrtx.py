class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        sqr_root = 0

        while left <= right:
            mid = (left + right)//2

            if mid*mid <= x:
                sqr_root = mid
                left = mid + 1
            else:
                right = mid - 1

        return sqr_root
        