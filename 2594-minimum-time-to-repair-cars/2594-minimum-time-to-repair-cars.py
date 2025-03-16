class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def can_repair(time: int)-> bool:
            total = 0
            for r in ranks:
                total += int(math.sqrt(time/r))

                if total >= cars:
                    return True

            return False
        
        left, right = 1, max(ranks) * cars * cars
        answer = right

        while left <= right:

            mid = (left + right) // 2

            if can_repair(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return answer