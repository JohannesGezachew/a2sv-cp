class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = Counter()
        ans = 0
        for char in s:
            counter[char] += 1

            if counter["R"] == counter["L"]:
                ans += 1
        return ans