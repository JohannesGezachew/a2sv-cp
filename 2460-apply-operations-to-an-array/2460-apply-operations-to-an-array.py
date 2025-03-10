from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] != 0 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        
        result.extend([0] * (n - len(result)))
        
        return result
