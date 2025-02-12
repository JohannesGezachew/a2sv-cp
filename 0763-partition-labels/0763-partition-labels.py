class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lelements = {l:i for i , l in enumerate(s)}
        left = right = 0
        ans = []

        for i,l in enumerate(s):
            left = max(left, lelements[l])
            if i == left:
                ans.append(i - right+ 1)
                right = i + 1 
        return ans

    