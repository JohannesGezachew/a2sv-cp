class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_so_far = -inf
        max_diff_so_far = -inf
        answer = 0 

        for num in nums:
            answer = max(answer, max_diff_so_far * num)
            max_diff_so_far = max(max_so_far - num, max_diff_so_far)
            max_so_far = max(max_so_far, num)
        
        return answer

