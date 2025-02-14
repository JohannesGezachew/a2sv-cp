class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = len(t)

        if len(s) < len(t):
            return ""

        ct = Counter(t)
        cs = Counter(s[: len(t)])
        mlen = len(t) if not (ct - cs) else inf
        ans = [] if (ct - cs) else [0, len(t) - 1]

        while right < len(s):
            cs[s[right]] += 1   
            while not (ct - cs):
                if mlen > (right - left + 1):
                    ans = [left, right]
                    mlen = right - left + 1

                cs[s[left]] -= 1
                if cs[s[left]] == 0:
                    del cs[s[left]]
                left += 1
            right += 1

        return s[ans[0] : ans[1] + 1] if ans else ""
