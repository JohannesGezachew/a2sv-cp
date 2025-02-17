class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        hashmap = {0: 1}
        
        for num in nums:
            cum_sum += num
            if cum_sum - k in hashmap:
                count += hashmap[cum_sum - k]
            if cum_sum not in hashmap:
                hashmap[cum_sum] = 0
            hashmap[cum_sum] += 1
        
        return count