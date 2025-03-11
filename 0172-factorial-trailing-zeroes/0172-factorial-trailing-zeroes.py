class Solution:
    def trailingZeroes(self, n: int) -> int:

        if n < 5 :
            return 0

        k = int(log(n)//log(5))
        ans = 0

        for i in range(1,k+1):
            ans += int(n //(5**i))
            
        return ans