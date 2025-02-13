class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        lon = 0
        pure = set()
        while right < len(s):
            while s[right] in pure:
                pure.remove(s[left])
                left += 1
            
            lon = max(lon, right -left +1)
            pure.add(s[right])
            right += 1
        return lon