class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)

        for i in range(len(nums)):
            prefix[i] += nums[i] + prefix[i-1]
        
        nums.reverse()
        for j in range(len(nums)):
            suffix[j] += suffix[j-1] + nums[j]
        suffix.reverse()

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1
        

            