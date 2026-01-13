class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        count = 0
        for i in range(1,len(points)):
            x_sum = abs(points[i][0] - points[i - 1][0])
            y_sum = abs(points[i][1] - points[i - 1][1])

            m = min(x_sum,y_sum)

            count += m +abs(y_sum-x_sum)
            print(count)

        return(abs(count))