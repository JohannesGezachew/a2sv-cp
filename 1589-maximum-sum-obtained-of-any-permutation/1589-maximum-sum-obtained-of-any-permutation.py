class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        freq = [0] * (n + 1)
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq.pop() 
        
        nums.sort()
        freq.sort() 
        max_sum = 0
        for num, f in zip(nums, freq):
            max_sum = (max_sum + num * f) % MOD
        
        return max_sum
