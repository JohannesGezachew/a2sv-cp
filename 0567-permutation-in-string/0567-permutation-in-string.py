class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        cs1 = Counter(s1)
        cs2 = Counter(s2[:right])
        res = 0

        while right < len(s2):
            if cs1 == cs2:
                return True
            cs2[s2[right]] += 1
            cs2[s2[left]] -= 1

            if cs2[s2[left]] == 0:
                cs2.pop(s2[left])
            left += 1
            right += 1

        return cs1 == cs2
