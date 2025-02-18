class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_count = Counter()
        prefix_count[0] = 1 

        for num in nums:
            prefix_sum += num
            count += prefix_count[prefix_sum - goal]
            prefix_count[prefix_sum] += 1
        
        return count