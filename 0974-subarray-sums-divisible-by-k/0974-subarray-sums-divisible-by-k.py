class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            remainder = (remainder + k) % k  
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return count
