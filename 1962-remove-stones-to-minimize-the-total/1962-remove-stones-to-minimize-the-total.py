class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            neg_max_pile = heapq.heappop(max_heap)
            max_pile = -neg_max_pile

            stones_to_remove = max_pile // 2
            new_pile = max_pile - stones_to_remove

            heapq.heappush(max_heap, -new_pile)

        final_sum = -sum(max_heap)
        return final_sum