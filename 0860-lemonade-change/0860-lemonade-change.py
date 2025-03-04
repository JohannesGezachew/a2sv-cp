class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = defaultdict(int)

        for cash in bills:
            if cash == 5:
                counter[5] += 1
            elif cash == 10:
                if counter[5] > 0:
                    counter[5] -= 1
                    counter[10] += 1
                else:
                    return False
            elif cash == 20:
                if counter[10] > 0 and counter[5] > 0:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
        return True
