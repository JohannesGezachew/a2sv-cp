class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                counter[prod] += 1
        
        ans = 0
        for k in counter.values():
            if k > 1:
                ans += 8 * (k * (k - 1) // 2)
        return ans
