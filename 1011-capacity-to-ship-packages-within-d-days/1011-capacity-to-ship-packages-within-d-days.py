class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        def canship(capacity):
            current_load, days_needed = 0, 1

            for weight in weights:

                if current_load + weight > capacity:
                    days_needed += 1
                    current_load =0

                current_load += weight
                
            return days_needed <= days

        while left < right:
            mid = left + (right-left)//2

            if canship(mid):
                right = mid 
            else:
                left = mid + 1
        return left
