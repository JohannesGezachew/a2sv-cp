class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        holder = colors + colors
        dic = dict()

        for i in range(1, k):
            if holder[i-1] == holder[i]:
                dic[i] = holder[i-1]
                
        ans = 0 if dic else 1 
        left = 0

        for i in range(1, len(colors)):
            if (left + 1) in dic:
                del dic[left + 1]
            
            j = i + k - 1
            if holder[j - 1] == holder[j]:
                dic[j] = holder[j - 1]
            
            if not dic:
                ans += 1
                
            left += 1
            
        return ans
