class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        m = (max(nums)+1)
        count = [0] * m
        result = []

        for i in range(len(nums)):
            count[nums[i]] += 1
            
        for index, value in enumerate(count):
            for j in range(value):
                result.append(index)

        return result


