class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        rem = 1
        leng = 1

        seen = set()
        while rem % k != 0:
            n = rem*10 + 1
            rem = n % k
            leng += 1

            if rem in seen:
                return -1
            else:
                seen.add(rem)
        return leng