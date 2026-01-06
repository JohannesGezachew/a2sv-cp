class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        total_sum = 0

        for x in nums:
            p = round(x ** (1/3))
            if p ** 3 == x and is_prime(p):
                total_sum += 1 + p + p*p + x
                continue

            for d in range(2, int(x ** 0.5) + 1):
                if x % d == 0:
                    e = x // d
                    if d != e and is_prime(d) and is_prime(e):
                        total_sum += 1 + d + e + x
                    break

        return total_sum