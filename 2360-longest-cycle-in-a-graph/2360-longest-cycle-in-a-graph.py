class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        answer = -1

        for i in range(n):
            if not visited[i]:
                node_to_step = {}
                step = 0
                current = i
                while current != -1:
                    if current in node_to_step:
                        answer = max(answer, step - node_to_step[current])
                        break
                    if visited[current]:
                        break
                    node_to_step[current] = step
                    visited[current] = True
                    current = edges[current]
                    step += 1
        return answer
