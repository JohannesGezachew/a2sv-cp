class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        counter = Counter()
        ans = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            if  s[right] == "0":
                ans += counter["1"]

        return ans
            