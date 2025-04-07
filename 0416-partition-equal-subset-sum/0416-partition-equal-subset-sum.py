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
                            
                #take 
                take = dp(idx + 1, curr_sum + nums[idx])
                #dont_take

                dont_take = dp(idx + 1, curr_sum)
                memo[(idx, curr_sum)] = take or dont_take

            return memo[(idx, curr_sum)]
        
        return dp(0, 0)

        
