class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        num = list(s)
        num.sort(reverse=True)
        one = num[0]
        num.append(one)
        return "".join(num[1:])
