class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def checker(n: int) -> bool:
            diff = [0] * (len(nums) + 1)
            for i in range(n):
                l, r, k = queries[i]
                diff[l] -= k
                if r + 1 < len(diff):
                    diff[r + 1] += k

            current = 0
            for i in range(len(nums)):
                current += diff[i]
                if nums[i] + current > 0:
                    return False
            return True

        lo, hi = 0, len(queries)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if checker(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
