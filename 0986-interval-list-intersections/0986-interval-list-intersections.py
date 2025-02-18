from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        left, right = 0, 0
        n, m = len(firstList), len(secondList)

        while left < n and right < m:
            startf, endf = firstList[left]
            starts, ends = secondList[right]

            start = max(startf, starts)
            end = min(endf, ends)

            if start <= end:
                result.append([start, end])
                
            if endf < ends:
                left += 1
            else:
                right += 1

        return result
