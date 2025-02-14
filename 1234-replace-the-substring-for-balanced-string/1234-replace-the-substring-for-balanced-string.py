class Solution:
    def balancedString(self, s: str) -> int:
        left = 0
        right = 0
        counter = Counter()
        ca = Counter(s)
        bal = len(s)//4
        ans = float("inf")
        holder = Counter()

        for key,val in ca.items():
            if val > bal:
                holder[key] = val -bal
        while right < len(s):
            counter[s[right]] += 1

            while left < len(s) and counter >= holder:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                ans = min(ans, right - left + 1)
                left += 1
            right += 1
        return ans
        