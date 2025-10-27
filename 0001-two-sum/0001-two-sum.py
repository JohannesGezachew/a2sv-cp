class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in x:
                return i , x.get(target-nums[i])
            x[nums[i]] = i
        
        