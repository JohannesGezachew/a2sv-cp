class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = {}
        
        def dfs(node, c):
            if node in color:
                return color[node] == c
            
            color[node] = c

            return all(dfs(nei, c^1) for nei in graph[node])
        
        for person in range(1,n+1):
            if person not in color:
                if not dfs(person,0):
                    return False
        
        return True
