class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        bought = 0
        current_cost = 0

        for cost in costs:
            current_cost += cost
            if current_cost <= coins:
                bought += 1
        return bought