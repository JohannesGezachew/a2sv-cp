class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        ans = 0
        while left < right:
            h = min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            ans = max(ans,h*(right-left+1) )

        return ans