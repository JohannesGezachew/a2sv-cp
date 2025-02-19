class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        holder = []
        n =len(score)
        m = len(score[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
                holder.append(score[i][k])
        holder.sort(reverse=True)
        di = {val:i for i, val in enumerate(holder)}

        for row in range(n):
            ans[di[score[row][k]]] = score[row]
        
        return ans