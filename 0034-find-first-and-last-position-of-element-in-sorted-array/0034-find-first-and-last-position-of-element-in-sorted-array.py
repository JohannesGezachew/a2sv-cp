class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftmost(nums, target):
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return pos

        def rightmost(nums, target):
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    pos = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return pos

        left_index = leftmost(nums, target)
        if left_index == -1 or nums[left_index] != target:
            return [-1, -1]

        right_index = rightmost(nums, target)
        return [left_index, right_index]
