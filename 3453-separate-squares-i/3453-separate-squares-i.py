class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        low = float('inf')
        high = 0

        for x, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)

        target = total_area / 2.0

        def area_below(h):
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += l * (h - y)
            return area

        for _ in range(60):
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low
