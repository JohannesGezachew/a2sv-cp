class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_lengths(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare_lengths))
        l = "".join(nums) 
        return l if l and int(l) != 0 else "0"