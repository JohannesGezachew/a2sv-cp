class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2

        memo = {}
        
        def dp(idx, curr_sum):
            if idx == len(nums):
                return curr_sum == target
            
            if (idx, curr_sum) not in memo:

                memo[(idx, curr_sum)] = dp(idx + 1, curr_sum + nums[idx]) or dp(idx + 1, curr_sum)

            return memo[(idx, curr_sum)]
        
        return dp(0, 0)

        
