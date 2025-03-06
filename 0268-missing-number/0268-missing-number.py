class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot_sum = sum(range(max(nums) + 1))
        curr_sum = sum(nums)
        ans = tot_sum - curr_sum

        if ans != 0:
            return ans
        
        if 0 not in nums:
            return 0
        
        return max(nums) + 1