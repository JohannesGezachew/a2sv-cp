class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        baskets = Counter()
        ans = 0

        while right < len(fruits):
            baskets[fruits[right]] += 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            ans = max(ans, right- left + 1)
            right += 1

        return ans
        
                