class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 0
        curr_mask = 0
        left = 0
        
        for right, num in enumerate(nums):
            while curr_mask & num:
                curr_mask &= ~nums[left]
                left += 1
            
            curr_mask |= num
        
            max_len = max(max_len, right - left + 1)
        
        return max_len
