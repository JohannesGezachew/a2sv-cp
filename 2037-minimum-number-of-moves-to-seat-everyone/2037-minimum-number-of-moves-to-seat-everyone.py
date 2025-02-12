class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        ans = 0 

        left  = 0
        right = 0
        while right < len(seats):
            ans += abs(seats[left] - students[right])
            left += 1
            right += 1
            
        return ans