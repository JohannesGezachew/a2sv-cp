class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        if n == 1:
            return ans
        else:
            for i in range(2,n+1):
                ans += 4*(i-1)
            return ans
        
