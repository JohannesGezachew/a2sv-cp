class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        perimeter = 0

        def dfs(r: int, c: int):
            nonlocal perimeter
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                perimeter += 1
                return

            if grid[r][c] == -1:
                return

            grid[r][c] = -1

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter

        return 0
