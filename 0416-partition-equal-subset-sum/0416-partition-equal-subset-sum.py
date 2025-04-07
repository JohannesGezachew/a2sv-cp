class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        @cache
        def dp(idx, curr_sum):
            if idx == len(nums):
                return curr_sum == target
            
            return dp(idx + 1, curr_sum + nums[idx]) or dp(idx + 1, curr_sum)

        
        return dp(0, 0)

        
