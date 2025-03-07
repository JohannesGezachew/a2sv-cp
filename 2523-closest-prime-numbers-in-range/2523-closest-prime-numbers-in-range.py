class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right+1, i):
                    sieve[j] = False

        primes = [i for i in range(max(2, left), right + 1) if sieve[i]]
    
        if len(primes) < 2:
            return [-1, -1]
        
        best_diff = float('inf')
        closest_pair = [-1, -1]
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < best_diff:
                best_diff = diff
                closest_pair = [primes[i-1], primes[i]]
        
        return closest_pair
