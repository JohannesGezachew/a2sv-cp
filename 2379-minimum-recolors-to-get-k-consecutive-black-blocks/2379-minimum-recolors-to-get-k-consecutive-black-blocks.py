class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks[:k])
        ans = counter["B"]
        left = 0
        for right in range(k,len(blocks)):
            counter[blocks[right]] += 1
            counter[blocks[left]] -= 1
            if  counter[blocks[left]] == 0:
                del counter[blocks[left]]
            left += 1
            ans = max(ans, counter["B"])
        if ans < k:
            return k - ans
        else:
            return 0
        