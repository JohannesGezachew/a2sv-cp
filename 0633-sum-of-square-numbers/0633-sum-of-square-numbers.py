class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = floor(sqrt(c))

        while left <= right:
            current_sum = pow(left,2) + pow(right,2)
            if current_sum < c:
                left += 1
            elif current_sum > c:
                right -= 1
            else:
                return True
        return False