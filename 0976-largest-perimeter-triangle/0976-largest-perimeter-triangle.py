class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        l = len(nums)
        perimeter = 0
        for i in range(0,l-2):
            if nums[i] < nums[i+1] +nums[i+2]:
                perimeter = nums[i] + nums[i+1] + nums[i+2]
                return perimeter
            
        return 0
    




