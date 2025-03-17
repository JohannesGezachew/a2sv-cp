class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        return all(count%2 == 0 for count in counter.values())
