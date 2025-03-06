class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        miss = 0
        rep = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                counter[grid[row][col]] += 1

        for i in range(1, len(counter)+1):
            if counter[i] == 0:
                miss = i
            elif counter[i] > 1:
                rep = i

        if rep == 0:
            rep = len(counter)
        if miss == 0:
            miss = len(counter)+1
            
        return [rep,miss]
                

        