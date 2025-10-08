class DynamicK:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def query(self, k: int) -> int:
        ans = 0
        T = 0
        freq = defaultdict(int)
        freq[0] = 1

        for x in self.nums:
            T += x
            ans += freq[T - k]
            freq[T] += 1
        return ans

    def add_k(self, current_k: int, delta: int) -> int:
        return self.query(current_k + delta)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return DynamicK(nums).query(k)
