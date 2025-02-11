class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        end = len(nums) - 1
        
        while right <= end:
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            elif nums[right] == 2:
                nums[right], nums[end] = nums[end], nums[right]
                end -= 1
            else:
                right += 1